from django import template

register = template.Library()


@register.filter
def split(value, sep=","):
    """Split a comma-separated string into a list, trimming whitespace."""
    if not value:
        return []
    return [v.strip() for v in value.split(sep)]