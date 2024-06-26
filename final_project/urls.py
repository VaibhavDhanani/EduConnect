"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from final_project import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login),
    path("home/", views.home, name='home'),
    path("class_details/<str:course_name>/", views.class_details, name='class_details'),
    path("lecture/<str:course_name>", views.lecture, name='lecture'),
    path("classes", views.classes, name='classes'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("notes", views.notes, name='notes'),
    path("", include("Class.urls")),
    path("Materials/<str:course_name>", views.materials, name='Materials'),
    path("Assignments/<str:course_name>", views.assignment, name='Assignments'),
    path("delete_submission/<int:sid>/<str:course_name>", views.delete_submission, name="delete_submission"),
    path("view_submission/<int:aid>/<str:course_name>",views.view_submission, name="view_submission"),
    path("delete_assignment/<int:assignment_id>/<str:course_name>", views.delete_assignment, name="delete_assignment"),
]
