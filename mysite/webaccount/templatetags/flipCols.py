from django import template
from webaccount.models import *
register = template.Library()
def flipCols(user_value):
    return user_value[::-1]

register.filter(flipCols)