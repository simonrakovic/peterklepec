__author__ = 'simon'

from django.template.defaulttags import register

@register.filter(name='dictionaryLookup')
def cut(value, arg):
    return value[arg]