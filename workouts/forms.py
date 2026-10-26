from django import forms
from .models import WorkoutSession

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ["routine",'date','duration_minutes','notes']
        labels = {
            "routine": "Routine",
            "date": "Workout Date",
            "duration_minutes":  "Duration (Minutes)",
            "notes": "Notes",
        }
        help_texts = {
            "routine": "Select the routine performed during this session.",
            "date": "Select the date when the workout took place.",
            "duration_minutes": "Enter the total duration of the workout in minutes.",
            "notes": "Optional notes, performance tracking, or comments about the session.",
        }
        error_messages = {
            "routine": {
                "required": "Please select a routine.",
            },
            "date": {
                "required": "Please enter a valid workout date.",
                "invalid": "Enter a valid date format (YYYY-MM-DD).",
            },
            "duration_minutes": {
                "required": "Please enter the duration in minutes.",
                "invalid": "Enter a valid whole number for the duration.",
            },
        }
        widgets = {
            "routine": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"},format="%Y-%m-%d",),
            "duration_minutes": forms.NumberInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4,
                                           'placeholder': "How did the workout feel? Any personal records?",}),
        }