from django import template
from django.template.defaultfilters import stringfilter

from ..utils.meal_types import MEAL_TYPES_DICT

register = template.Library()


@register.filter
@stringfilter
def meal_type_stringifier(key):
    return MEAL_TYPES_DICT.get(key)
