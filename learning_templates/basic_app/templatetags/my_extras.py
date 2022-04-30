from atexit import register
from django import template

register = template.Library()

# @register.filter(name='cut')
def cut(value, arg):
    # This cuts out all values of arg from the string

    return value.replace(arg, '')

register.filter('cut', cut)
# First one is the name of the filter and the second is the function of the filter itself

