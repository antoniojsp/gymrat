from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Date


class ListListView(ListView):
    model = Date
    template_name = "journal/index.html"