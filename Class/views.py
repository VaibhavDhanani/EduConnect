from django.shortcuts import redirect, render
import random
import string
from .models import Class
from django.urls import reverse


# Create your views here.


def generate_random_code(length=10):
    while True:
        code = "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not Class.objects.filter(code=code).exists():
            return code


def generate_random_code(length=10):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def create_new_class(request):
    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        teacher_name = request.POST.get("teacher_name")
        if subject_name and teacher_name:
            code = generate_random_code()
            new_class = Class.objects.create(
                code=code, subject=subject_name, teachername=teacher_name
            )
            return redirect(reverse('classes'))
        else:
            return render(request, "aboutus.html")
    else:
        classes = Class.objects.all()
        return render(request, "lecture.html", {"classes": classes})
