from django.contrib import admin
from .models import Profile, Skill, Experience, Project, ContactMessage


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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'technologies',
        'is_featured',
        'display_order',
    )

    list_editable = (
        'is_featured',
        'display_order',
    )

    search_fields = (
        'name',
        'description',
        'technologies',
    )

    list_filter = (
        'is_featured',
    )

    ordering = (
        'display_order',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'created_at',
        'is_read',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'message',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    list_editable = (
        'is_read',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )