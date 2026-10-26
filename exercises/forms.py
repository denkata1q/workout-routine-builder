from django import forms
from .models import Exercise,MuscleGroup
class NameCleanMixin:
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            name = ' '.join(name.split())
            if name.isdigit():
                verbose_name=self.Meta.model._meta.verbose_name
                raise forms.ValidationError(
                    f"{verbose_name.capitalize()} name cannot consist only of numbers."
                )
        return name

class MuscleGroupForm(NameCleanMixin, forms.ModelForm):

    class Meta:
        model = MuscleGroup
        fields = ["name"]
        labels = {
            "name": "Muscle Group Name",
        }
        help_texts = {
            "name": "Enter a unique name for the muscle group.",
        }
        error_messages = {
            "name": {
                "required": "Please enter a muscle group name.",
            }
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "e.g., Chest, Quadriceps, Biceps",
                    "class": "form-control",
                }
            ),
        }

class ExerciseForm(NameCleanMixin,forms.ModelForm):
    created_on = forms.DateTimeField(
        disabled=True,
        required=False,
        label='Created on',
        help_text="This timestamp is automatically generated and cannot be modified.",
        widget=forms.DateTimeInput(attrs={"class": "form-control"}),
    )
    class Meta:
        model = Exercise
        fields = ['name','description','difficulty','muscle_groups']
        labels = {
            "name": "Exercise Name",
            "description": "Description",
            "difficulty": "Difficulty Level",
            "muscle_groups": "Muscle Groups",
        }

        help_texts = {
            "name": "Enter the name of the exercise",
            "description": "Enter the description of the exercise",
            "difficulty": "Enter the difficulty of the exercise",
            "muscle_groups": "Enter the muscle groups of the exercise",
        }

        error_messages = {
            "name": {
                "required": "Please enter the name of the exercise"},

            'difficulty': {
                'required': 'Please enter the difficulty of the exercise'
            },
            'muscle_groups': {
                'required': 'Please enter the muscle groups of the exercise'
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Squat'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'difficulty' : forms.Select(attrs={'class': 'form-select'}),
            'muscle_groups': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            if self.instance and self.instance.pk:
                self.fields["created_on"].initial = self.instance.created_on
            else:
                self.fields.pop("created_on", None)

