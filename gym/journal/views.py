from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
# Create your views here.
from .models import Date, Exercise


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
        context["date"] = Exercise.objects.get(id=self.kwargs["list_id"])
        return context

class DateCreate(CreateView):
    model = Date
    fields = ["date"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new date"
        return context