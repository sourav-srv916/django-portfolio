from django.shortcuts import render
from .models import Profile, Skill, Experience


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    return render(request, 'main/home.html', {'profile': profile, 'skills': skills, 'experiences': experiences})