from django import template

register = template.Library()


@register.filter
def split_technologies(value):
    if not value:
        return []

    return [technology.strip() for technology in value.split(",")]