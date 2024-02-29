from django.shortcuts import render
from Class.models import *


def login(request):
    return render(request, "login.html")


def home(request):
    if "name" in request.COOKIES:
        if request.COOKIES.get("role") == "Teacher":
            record = Teacher(
                id=request.COOKIES.get("uid"), name=request.COOKIES.get("name")
            )
            record.save()
        elif request.COOKIES.get("role") == "Student":
            record = Student(
                id=request.COOKIES.get("uid"), name=request.COOKIES.get("name")
            )
            record.save()
    return render(request, "home.html")


def classes(request):
    classes = Class.objects.all()
    return render(request, "classes.html", context={"classes": classes})


def class_details(request,course_name):
    context = {'course_name': course_name}
    return render(request, "class_details.html", context)

def lecture(request,course_name):
    classes = Class.objects.all()
    lectures = Lecture.objects.all()
    context = {
        'course_name': course_name,
        'classes': classes,
        'lectures': lectures
    }
    return render(request, "lecture.html", context)


def assignment(request):
    return render(request, "assignment.html")


def result(request):
    return render(request, "results.html")


def aboutus(request):
    return render(request, "aboutus.html")


def notes(request):
    return render(request, "notes.html")
