from django import template
from Class.models import Submission
from django import template

register = template.Library()

@register.filter
def is_late_submission(current_date, due_date):
    return current_date > due_date


@register.simple_tag
def break_loop():
    return None

@register.filter
def get_submission_by_student_id(submissions, student_id):
    try:
        return submissions.filter(student_id=student_id).first()
    except Submission.DoesNotExist:
        return None


