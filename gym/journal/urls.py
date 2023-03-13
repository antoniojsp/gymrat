# todo_list/todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.DatesListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ExerciseListView.as_view(), name="list"),
    path("list/add/", views.DateCreate.as_view(), name="list-add"),

]