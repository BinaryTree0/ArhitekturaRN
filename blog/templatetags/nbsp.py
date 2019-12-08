import re

from django import template
register = template.Library()

@register.filter
def nbsp (string):
    return re.sub("&", "&nbsp;", string )
