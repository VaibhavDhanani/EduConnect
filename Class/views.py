from django.shortcuts import redirect, render

from .models import Class


# Create your views here.
def create_new_class(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        teacher_name = request.POST.get('teacher_name')
        if subject_name and teacher_name:
            new_class = Class.objects.create(subject=subject_name, teachername=teacher_name)
            return redirect('classes.html')  
        else:
            return render(request, 'aboutus.html')
    else:
        return render(request, 'lecture.html')