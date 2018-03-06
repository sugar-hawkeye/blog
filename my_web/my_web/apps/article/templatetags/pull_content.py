from django import template

from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.template.defaultfilters import stringfilter

from my_web.libs.Utils import read_md


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def pull_content(value):
    content = read_md(value)
    return mark_safe(force_text(content,'utf-8'))