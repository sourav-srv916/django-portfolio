from django.contrib import admin
from .models import Profile, Skill, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'email',
        'location',
    )

    search_fields = (
        'name',
        'title',
        'email',
        'location',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'level',
        'display_order',
    )

    search_fields = (
        'name',
        'category',
        'level',
    )

    list_filter = (
        'category',
        'level',
    )

    ordering = (
        'display_order',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company',
        'start_date',
        'end_date',
        'display_order',
    )

    search_fields = (
        'job_title',
        'company',
        'description',
    )

    ordering = (
        'display_order',
    )