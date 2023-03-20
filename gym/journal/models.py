from django.db import models

from django.utils import timezone

from django.db import models
from django.urls import reverse
from datetime import datetime


class Date(models.Model):
    date = models.DateField(unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return str(self.date)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.date.id), str(self.id)]
        )

    def __str__(self):
        return f"Name: {self.name}, Weight:{self.weight} lb. ,Sets: {self.sets}, Reps: {self.reps}"

    class Meta:
        ordering = ["name"]
