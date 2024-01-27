from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def classes(request):
    return render(request,"classes.html")

def class_details(request):
    return render(request,"class_details.html")

def lecture(request):
    return render(request,"lecture.html")

def assignment(request):
    return render(request,"assignment.html")

def result(request):
    return render(request,"results.html")

def aboutus(request):
    return render(request,"aboutus.html")

def notes(request):
    return render(request,"notes.html")