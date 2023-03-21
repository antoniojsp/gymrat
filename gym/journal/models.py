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
        date = datetime.strptime(str(self.date),
                                 "%Y-%m-%d")

        return date.strftime("%A, %B %d, %Y")


class NewExercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Exercise(models.Model):
    name = models.ForeignKey(NewExercise, on_delete=models.SET_NULL, null=True)

    # name = models.CharField(max_length=100, )
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
