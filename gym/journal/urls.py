# todo_list/todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.DatesListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ExerciseListView.as_view(), name="list"),
    path("list/add/", views.DateCreate.as_view(), name="list-add"),
    path(
        "list/<int:pk>/delete/", views.DateDelete.as_view(), name="list-delete"
    ),
    path(
        "list/<int:list_id>/item/add/",
        views.ExerciseCreate.as_view(),
        name="item-add",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ExerciseDelete.as_view(),
        name="item-delete",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ExerciseUpdate.as_view(),
        name="item-update",
    ),
    path(
        "exercise/add/", views.NewExerciseCreate.as_view(), name="exercise-create",
    )

]