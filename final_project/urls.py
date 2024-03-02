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
    path("home.html", views.home, name='home'),
    path("class_details/<str:course_name>/", views.class_details, name='class_details'),
    path("lecture/<str:course_name>", views.lecture, name='lecture'),
    path("classes", views.classes, name='classes'),
    path("assignment.html", views.assignment),
    path("results", views.result, name='results'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("notes", views.notes, name='notes'),
    path("", include("Class.urls")),
    path("Materials", views.materials, name='Materials'),
]
