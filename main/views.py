import logging
import secrets
import hashlib
import json
import os

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import (Profile, Skill, Experience, Project, ContactMessage,)
from django.core.mail import send_mail
from django.conf import settings

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.cache import cache


logger = logging.getLogger(__name__)


def send_brevo_email(name, email, phone, message):

    api_key = os.getenv('BREVO_API_KEY')
    sender_email = os.getenv('BREVO_SENDER_EMAIL')
    notification_email = os.getenv('CONTACT_NOTIFICATION_EMAIL')

    if not all([api_key, sender_email, notification_email]):
        raise ValueError('Brevo email configuration is incomplete.')

    payload = {
        'sender': {
            'name': 'Django Portfolio',
            'email': sender_email,
        },
        'to': [
            {'email': notification_email}
        ],
        'replyTo': {
            'email': email,
            'name': name,
        },
        'subject': f'New Portfolio Message from {name}',
        'textContent': (
            'You have received a new message through your portfolio.\n\n'
            f'Name: {name}\n'
            f'Email: {email}\n'
            f'Phone: {phone}\n\n'
            f'Message:\n{message}'
        ),
    }

    request = Request(
        'https://api.brevo.com/v3/smtp/email',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'api-key': api_key,
            'accept': 'application/json',
            'content-type': 'application/json',
        },
        method='POST',
    )

    with urlopen(request, timeout=15) as response:
        if response.status != 201:
            raise RuntimeError(
                f'Brevo returned unexpected status: {response.status}'
            )

        
# Contact Form Rate Limiting
CONTACT_RATE_LIMIT = 3
CONTACT_RATE_TIMEOUT = 600  # 10 minutes


def get_client_ip(request):

    return request.META.get('REMOTE_ADDR', 'unknown')


def is_contact_rate_limited(request):

    ip_address = get_client_ip(request)

    # Hash the IP address before using it as a cache key
    ip_hash = hashlib.sha256(
        ip_address.encode()
    ).hexdigest()

    cache_key = f'contact_rate_limit_{ip_hash}'

    # Start the counter for a new visitor
    if cache.add(
        cache_key,
        1,
        timeout=CONTACT_RATE_TIMEOUT
    ):
        return False

    # Increase the existing submission counter
    try:
        submission_count = cache.incr(cache_key)

    except ValueError:
        # Handle the unlikely case where the cache expires
        # between checking and incrementing
        cache.add(
            cache_key,
            1,
            timeout=CONTACT_RATE_TIMEOUT
        )
        return False

    return submission_count > CONTACT_RATE_LIMIT


def home(request):

    # Generate a unique token for each contact form
    if request.method == 'GET':

        contact_form_token = secrets.token_urlsafe(32)

        tokens = request.session.get('contact_form_tokens', [])

        tokens.append(contact_form_token)

        # Keep only the latest 10 tokens
        request.session['contact_form_tokens'] = tokens[-10:]

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.filter(is_featured=True)[:4]

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()
        honeypot = request.POST.get('portfolio_website', '').strip()

        if honeypot:
            return redirect('/#contact')

        # Duplicate Submission Protection
        submitted_token = request.POST.get('submission_token', '')

        tokens = request.session.get('contact_form_tokens', [])

        if not submitted_token or submitted_token not in tokens:

            messages.error(
                request,
                'This form has already been submitted. Please try again.'
            )

            return redirect('/#contact')

        # Consume the submitted token
        tokens.remove(submitted_token)

        # Generate a fresh token for the next form
        contact_form_token = secrets.token_urlsafe(32)

        tokens.append(contact_form_token)

        request.session['contact_form_tokens'] = tokens[-10:]


        if not all([name, email, phone, message]):

            messages.error(request, 'Please fill in all required fields.')

        else:
            try:
                validate_email(email)

            except ValidationError:
                messages.error(
                    request,
                    'Please enter a valid email address.'
                )
                return redirect('/#contact')


            # Rate Limiting
            if is_contact_rate_limited(request):

                messages.error(
                    request,
                    'You have reached the maximum number of submissions. Please try again after 10 minutes.'
                )

                return redirect('/#contact')

            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )

            try:
                if settings.EMAIL_PROVIDER == 'brevo':

                    # Production: Brevo HTTPS API
                    send_brevo_email(
                        name=name,
                        email=email,
                        phone=phone,
                        message=message,
                    )

                else:

                    # Local development: Gmail SMTP
                    send_mail(
                        subject=f'New Portfolio Message from {name}',

                        message=(
                            'You have received a new message through your portfolio.\n\n'
                            f'Name: {name}\n'
                            f'Email: {email}\n'
                            f'Phone: {phone}\n\n'
                            f'Message:\n{message}'
                        ),

                        from_email=None,

                        recipient_list=[settings.EMAIL_HOST_USER],

                        fail_silently=False,
                    )

            except Exception:
                logger.exception(
                    "Email notification failed for contact message from %s",
                    name
                )

            messages.success(
                request,
                "Thank you for contacting me. Your message has been received successfully. "
                "I'll get back to you as soon as possible."
            )

            return redirect('/#contact')

    return render(
        request,
        'main/home.html',
        {
            'profile': profile,
            'skills': skills,
            'experiences': experiences,
            'projects': projects,
            'contact_form_token': contact_form_token,
        }
    )


def all_projects(request):

    projects = Project.objects.all()

    paginator = Paginator(projects, 6)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'page_obj': page_obj,
        'projects': page_obj,
        'total_projects': paginator.count,
    }

    return render(request, 'main/all_projects.html', context)