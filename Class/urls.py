from django.urls import include, path

from Class import views
urlpatterns = [
    path('create_new_class',views.create_new_class),
]
