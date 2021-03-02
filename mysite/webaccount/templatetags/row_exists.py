from django import template
from webaccount.models import *
register = template.Library()
def row_exists(user_value):
    # return (for i in user_value)
    return True

register.filter(row_exists)