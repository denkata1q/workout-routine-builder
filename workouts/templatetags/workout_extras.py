from django import template

register = template.Library()
@register.filter
def duration_display(value):
    if value is None:
     return value
    try:
        minutes = int(value)
    except (ValueError,TypeError):
        return value
    if minutes == 0:
        return '0m'
    hours, rem_minutes = divmod(minutes, 60)
    parts=[]
    if hours > 0:
        parts.append(f"{hours}h")
    if rem_minutes > 0:
        parts.append(f"{rem_minutes}m")

    return " ".join(parts)

