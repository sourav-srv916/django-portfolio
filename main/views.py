from django.shortcuts import render
from .models import Profile, Skill


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()

    return render(request, 'main/home.html', {'profile': profile, 'skills': skills})