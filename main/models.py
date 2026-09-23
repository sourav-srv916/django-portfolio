from django.db import models

# Create your models here.
from django.db import models


class Profile(models.Model):

    name = models.CharField(max_length=100)

    title = models.CharField(max_length=150)

    introduction = models.TextField()

    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=150)

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    about = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):

    name = models.CharField(max_length=100)

    category = models.CharField(max_length=100, blank=True)

    level = models.CharField(max_length=50, blank=True)

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Experience(models.Model):

    job_title = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    start_date = models.CharField(max_length=50)

    end_date = models.CharField(max_length=50)

    description = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.job_title} - {self.company}"