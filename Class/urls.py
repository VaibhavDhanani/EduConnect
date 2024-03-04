from django.urls import include, path

from Class import views

urlpatterns = [
    path("home/create_new_class/", views.create_new_class),
    path("home/create_new_lecture", views.create_new_lecture, name="create_new_lecture"),
    path("home/create_new_assignment", views.create_new_assignment, name="create_new_assignment"),
    path("home/new_material_upload", views.new_material_upload, name="new_material_upload"),
]
