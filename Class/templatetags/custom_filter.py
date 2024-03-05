from django import template
from datetime import datetime,date

register = template.Library()

@register.filter
def is_late_submission(current_date, due_date):
    return current_date > due_date


