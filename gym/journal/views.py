from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
from .models import Date, Exercise, NewExercise


class DatesListView(ListView):
    model = Date
    template_name = "journal/index.html"

class ExerciseListView(ListView):
    model = Exercise
    template_name = "journal/date.html"

    def get_queryset(self):
        return Exercise.objects.filter(date_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = Date.objects.get(id=self.kwargs["list_id"])
        return context


class DateCreate(CreateView):
    model = Date
    fields = ["date"]

    def get_context_data(self):
        context = super(DateCreate, self).get_context_data()
        context["title"] = "Add a new date"
        return context


class NewExerciseCreate(CreateView):
    model = NewExercise
    fields = ["name"]

    def get_context_data(self):
        context = super(NewExerciseCreate, self).get_context_data()
        context["title"] = "Add a new exercise"
        return context

    success_url = reverse_lazy("index")

class ExerciseCreate(CreateView):
    model = Exercise
    fields = [
        "date",
        "name",
        "weight",
        "sets",
        "reps",
    ]

    def get_initial(self):
        initial_data = super(ExerciseCreate, self).get_initial()
        date_list = Date.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = date_list
        return initial_data

    def get_context_data(self):
        context = super(ExerciseCreate, self).get_context_data()
        date_list = Date.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = date_list
        context["title"] = "Enter a new exercise."
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.date_id])


class ExerciseUpdate(UpdateView):
    model = Exercise
    fields = [
        "date",
        "name",
        "weight",
        "sets",
        "reps",
    ]

    def get_context_data(self):
        context = super(ExerciseUpdate, self).get_context_data()
        context["todo_list"] = self.object.date
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class DateDelete(DeleteView):
    model = Date
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ExerciseDelete(DeleteView):
    model = Exercise

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.date
        return context

