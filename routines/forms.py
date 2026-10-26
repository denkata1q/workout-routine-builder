from django import forms
from .models import Routine
from exercises.forms import NameCleanMixin


class RoutineForm(NameCleanMixin, forms.ModelForm):

    class Meta:
        model = Routine
        fields = ['name', 'goal', 'description', 'exercises']
        labels = {
            'name': 'Routine Name',
            'goal': 'Goal',
            'description': 'Description',
            'exercises': 'Exercises',
        }
        help_texts = {
            "name": "Enter the name of the routine.",
            "goal": "Select the primary fitness goal of the routine.",
            "description": "Optional description or details about the routine.",
            "exercises": "Select the exercises included in this routine.",
        }
        error_messages = {
            "name": {
                'required': "The routine name is required.",
            },
            'goal': {
                'required': "Please select a goal",

            },
            'exercises': {
                'required': 'Select at least one exercise.',
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g., Upper Body Strength"}),
            "goal": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter routine notes or guidelines...",
                    "rows": 4,
                    "class": "form-control",
                }
            ),
            "exercises": forms.CheckboxSelectMultiple(),
        }
