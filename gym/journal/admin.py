from django.contrib import admin

# Register your models here.
from .models import Date, Exercise, NewExercise


class DateAdmin(admin.ModelAdmin):

    list_display = ["date"]

class ExerciseAdmin(admin.ModelAdmin):

    list_display = ("name", "weight", "sets", "reps", "date")

class AddAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Date, DateAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(NewExercise, AddAdmin)
