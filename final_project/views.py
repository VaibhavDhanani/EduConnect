from django.shortcuts import render
from Class.models import *
from django.http import HttpResponse


def login(request):
    return render(request, "login.html")


def home(request):
    if "name" in request.COOKIES:
        if request.COOKIES.get("role") == "Teacher":
            record = Teacher(
                id=request.COOKIES.get("uid"), name=request.COOKIES.get("name")
            )
            record.save()
            return render(request, "classes.html")
        elif request.COOKIES.get("role") == "Student":
            record = Student(
                id=request.COOKIES.get("uid"), name=request.COOKIES.get("name")
            )
            record.save()
            return render(request, "")  # // Student class code to add here
    elif "uid" in request.COOKIES:
        uid = request.COOKIES.get("uid")
        t_uid = Teacher.objects.filter(id=uid)
        if t_uid.exists():
            return render(request, "classes.html")

        s_uid = Student.objects.filter(id=uid)
        if s_uid.exists():
            return render(request, "")  # // Student class code to add here
    else:
        return render(request, "login.html")


def classes(request):
    classes = Class.objects.all()

    # Create the base HTTP response object
    response = render(request, "classes.html", context={"classes": classes})

    if "code" in request.COOKIES:
        response.delete_cookie("code")

    return response


def class_details(request, course_name):
    context = {'course_name': course_name}
    return render(request, "class_details.html", context)


def lecture(request, course_name):
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


def materials(request):
    return render(request, "Materials.html")


def new_material_upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        link = request.POST.get('url')
        code = request.COOKIES.get('code')
        class_obj = Class.objects.get(code=code)
        if code and title and link:
            material = Material(
                title=title, link=link, class_id=class_obj
            )
            material.save()
            return render(request, "Materials.html")
        return render(request, "Materials.html")
