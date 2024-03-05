from django.shortcuts import redirect, render
import random
import string
from .models import *
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
            return redirect(reverse("classes"))
        else:
            return render(request, "aboutus.html")
    else:
        classes = Class.objects.all()
        return render(request, "lecture.html", {"classes": classes})


def create_new_lecture(request):
    if request.method == "POST":
        title = request.POST.get("lecture_title")
        class_name_str = request.POST.get("class_name")
        try:
            class_instance = Class.objects.get(subject=class_name_str)
        except Class.DoesNotExist:
            return render(
                request, "error_page.html", {"message": "Class does not exist"}
            )

        lec_link = request.POST.get("lecture_link")

        if title and class_instance and lec_link:
            new_lecture = Lecture.objects.create(
                title=title, class_name=class_instance, link=lec_link
            )
            return redirect(reverse("lecture", kwargs={"course_name": class_name_str}))
        else:
            return render(
                request, "error_page.html", {"message": "Missing required fields"}
            )
    else:
        return render(request, "error_page.html", {"message": "Invalid request method"})


def new_material_upload(request):
    if request.method == "POST":
        title = request.POST.get("title")
        link = request.POST.get("url")
        code = request.COOKIES.get("code")
        class_obj = Class.objects.get(code=code)
        if code and title and link:
            material = Material(title=title, link=link, class_id=class_obj)
            material.save()
            return redirect(reverse("Materials", kwargs={"course_name": class_obj.subject}))
        return render(request, "home.html")


def create_new_assignment(request):
    if request.method == "POST":
        title = request.POST.get("assignment_title")
        date = request.POST.get("sub_date")
        class_name = request.POST.get("class_name")
        class_obj = Class.objects.get(subject=class_name)
        if date and title and class_name:
            assignment = Assignment(title=title, date=date, class_name=class_obj)
            assignment.save()
            return redirect(reverse("Assignments", kwargs={"course_name": class_name}))
        return render(request, "home.html")
    



