from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
import re

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    text = md.markdown(value, extensions=['markdown.extensions.extra'])
    text = re.sub('\d\.', '', text)
    return text
