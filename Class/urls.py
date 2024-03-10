from django.urls import include, path

from Class import views

urlpatterns = [
    path("create_new_class", views.create_new_class, name="create_new_class"),
    path("delete_class/<str:class_name>", views.delete_class, name="delete_class"),
    path("create_new_lecture", views.create_new_lecture, name="create_new_lecture"),
    path("create_new_assignment", views.create_new_assignment, name="create_new_assignment"),
    path("new_material_upload", views.new_material_upload, name="new_material_upload"),
    path("delete_material/<int:material_id>", views.delete_material, name="delete_material"),
    path("delete_lecture/<int:lec_id>", views.delete_lecture, name="delete_lecture"),
    path("join_class", views.join_class, name="join_class"),
]
