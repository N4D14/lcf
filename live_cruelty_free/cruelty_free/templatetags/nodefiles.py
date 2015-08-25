from django import template
from django.conf import settings

import os

register = template.Library()

@register.simple_tag
def node(file_name):
    return os.path.join(settings.BASE_DIR, 'node_modules/' + file_name)
