from django import template
from blog.models import Status

# https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/
register = template.Library()


@register.simple_tag()
def get_status_question():
    return Status.objects.all()
