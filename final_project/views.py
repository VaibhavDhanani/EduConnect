from django.shortcuts import render, redirect
from Class.models import *
from django.http import HttpResponse
import ntplib
from datetime import datetime, date


def login(request):
    return render(request, "login.html")


def home(request):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")

    if "name" in request.COOKIES:
        if request.COOKIES.get("role") == "Teacher":
            record = Teacher(
                id=request.COOKIES.get("uid"), name=request.COOKIES.get("name")
            )
            record.save()
            return render(request, "home.html", {"name": request.COOKIES.get("name"), "role": "Teacher"})
        elif request.COOKIES.get("role") == "Student":
            record = Student(
                id=request.COOKIES.get("uid"), name=request.COOKIES.get("name")
            )
            record.save()
            return render(request, "home.html", {"name": request.COOKIES.get("name"), "role": "Student"})
    else:
        return render(request, "login.html")


def classes(request):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")

    classes = Class.objects.all()
    role = request.user_role
    name = request.COOKIES.get("name")
    class_codes = []
    print(role)

    if role == "Teacher":
        all_codes = Class_Teacher.objects.filter(teacher_id=request.user_id)
        for codes in all_codes:
            record = Class.objects.get(code=codes.class_id.code)
            class_codes.append(record)

    elif role == "Student":
        all_codes = Class_Student.objects.filter(student_id=request.user_id)
        for codes in all_codes:
            record = Class.objects.get(code=codes.class_id.code)
            class_codes.append(record)
    # Create the base HTTP response object
    response = render(request, "classes.html", context={"classes": class_codes, "name": name})

    if "code" in request.COOKIES:
        response.delete_cookie("code")

    return response


def class_details(request, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    context = {'course_name': course_name}
    return render(request, "class_details.html", context)


def lecture(request, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    classes = Class.objects.all()
    lectures = Lecture.objects.filter()
    context = {
        'course_name': course_name,
        'classes': classes,
        'lectures': lectures
    }
    return render(request, "lecture.html", context)


def get_current_date_ntp():
    ntp_client = ntplib.NTPClient()
    ntp_server = 'pool.ntp.org'

    try:
        response = ntp_client.request(ntp_server)
        current_time = datetime.utcfromtimestamp(response.tx_time)
        current_date = current_time.date()
        return current_date
    except Exception as e:
        print("An error occurred while getting current date from NTP server:", str(e))
        current_date = date.today()  # Use the date class here
        return current_date


def assignment(request, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    current_date = get_current_date_ntp()
    context = {}
    if request.user_role == "Teacher":
        assignments = Assignment.objects.filter(class_name__subject=course_name)
        context = {'course_name': course_name, 'assignments': assignments, "current_date": current_date}

    elif request.user_role == "Student":
        sub_set = {}
        assignments = Assignment.objects.filter(class_name__subject=course_name).prefetch_related('submission_set')
        asmt = Assignment.objects.filter(class_name__subject=course_name)

        cnt = 0
        submission_link = ''
        for x in assignments:
            print(x.submission_set.filter(student_id=request.user_id).first())
            obj = x.submission_set.filter(student_id=request.user_id).first()
            if obj is not None:
                submission_link = obj.link
                sub_set[x.asgmt_id] = {'link': submission_link, 'id': obj.sub_id, 'name': obj.name}
            else:
                print(None)
                submission_link = ''

        print(sub_set)
        if len(sub_set) == 0:
            sub_set = {'None': 'None'}

        context = {'course_name': course_name, 'assignments': asmt, "current_date": current_date,
                   "sub_set": sub_set}

    return render(request, "assignment.html", context)


def aboutus(request):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    return render(request, "aboutus.html")


def notes(request):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    materials = Material.objects.all()
    context = {"materials": materials}
    return render(request, "notes.html", context)


def materials(request, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    materials = Material.objects.all()
    class_data = Class.objects.filter(subject=course_name).first()
    context = {"materials": materials, "class_code": class_data}
    return render(request, "Materials.html", context)


def delete_submission(request, sid, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    obj = Submission.objects.filter(sub_id=sid)
    obj.delete()
    return assignment(request, course_name)


def view_submission(request, aid, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    obj = Submission.objects.filter(asgmt_id=aid).filter(asgmt_id__class_name__subject=course_name)
    asmt_date = Assignment.objects.get(asgmt_id=aid).date
    class_obj = Class.objects.get(subject=course_name)
    student_ids = Class_Student.objects.filter(class_id=class_obj.code).values_list('student_id', flat=True)
    students = Student.objects.filter(id__in=student_ids)
    context = {"students": students, "submissions": obj, "sub_date": asmt_date, "course_name": course_name}
    return render(request, "submission.html", context)


def delete_assignment(request, assignment_id, course_name):
    if request.user_role == "default" or request.user_id == "default" or request.user_name == "default":
        return redirect("/")
    Assignment.objects.filter(asgmt_id=assignment_id).delete()
    Submission.objects.filter(asgmt_id=assignment_id).delete()
    # return redirect(request, "/Assignments/" + course_name)
    return redirect("/Assignments/" + course_name)
