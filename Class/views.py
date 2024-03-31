from django.shortcuts import redirect, render
import random
import string
from .models import *
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

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
            try:
                code = generate_random_code()
                new_class = Class.objects.create(
                    code=code, subject=subject_name, teachername=teacher_name
                )
                t_id = request.user_id
                teacher = Teacher.objects.get(id=t_id)
                record = Class_Teacher(class_id=new_class, teacher_id=teacher)
                record.save()
                messages.info(request, "Class Created\n Class code:- {code}")
                return HttpResponseRedirect(reverse("classes"))
            except IntegrityError:
                messages.error(request, "Class with the same details already exists.")
                return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "home.html")
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
        file_name = request.FILES.get("file").name
        code = request.COOKIES.get("code")

        class_obj = Class.objects.get(code=code)

        if code and title and link and file_name:
            material = Material(title=title, link=link, class_id=class_obj, name=file_name)
            material.save()
            return redirect(reverse("Materials", kwargs={"course_name": class_obj.subject}))
        return render(request, "Materials.html")


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


def delete_material(request, material_id):
    material = Material.objects.get(material_id=material_id)
    course_name = material.class_id.subject
    material.delete()
    return redirect(reverse("Materials", kwargs={"course_name": course_name}))


def delete_class(request, class_name):
    Class.objects.filter(subject=class_name).delete()
    return redirect(reverse("classes"))


def delete_lecture(request, lec_id):
    lec = Lecture.objects.get(lec_id=lec_id)
    course_name = lec.class_name.subject
    lec.delete()
    return redirect(reverse("lecture", kwargs={"course_name": course_name}))


def join_class(request):
    if request.method == "POST":
        code = request.POST.get("class_code")

        if code:
            try:
                get_class = Class.objects.get(code=code)
                user = Student.objects.get(id=request.user_id)
                record = Class_Student(class_id=get_class, student_id=user)
                record.save()
                return redirect(reverse("classes"))
            except ObjectDoesNotExist:
                messages.error(request, "Class does not exist.")
                return HttpResponseRedirect(reverse("home"))
            except IntegrityError:
                messages.error(request, "You are already enrolled in this class.")
                return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request, "Please provide appropriate Code")
            return HttpResponseRedirect(reverse("home"))
            


def assignment_upload(request):
    if request.method == "POST":
        s_id = request.user_id
        student = Student.objects.get(id=s_id)
        a_id = request.POST.get("asmt_id")
        assignment = Assignment.objects.get(asgmt_id=a_id)
        file_name = request.POST.get("file_name")
        link = request.POST.get("url")

        print(file_name, link, s_id , a_id)
        if file_name and link:
            submission = Submission(asgmt_id=assignment, student_id=student, link=link, name=file_name)
            submission.save()
            return redirect(reverse("Assignments", kwargs={"course_name": assignment.class_name.subject}))
        else:
            messages.error(request, "Missing fields requried ")
            return HttpResponseRedirect(reverse("home"))

