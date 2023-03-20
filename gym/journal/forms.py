# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import NewExercise


# create a ModelForm
class NewExerciseForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = NewExercise
        fields = "__all__"