

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from routines.models import Routine


def validate_not_in_future(value):
    """Validator to ensure a date is not set in the future."""
    if value > timezone.localdate():
        raise ValidationError(
            'The workout date cannot be in the future.'
        )


class WorkoutSession(models.Model):
    routine = models.ForeignKey(Routine,
        on_delete=models.CASCADE,
        related_name='workout_sessions',
        verbose_name='Routine',
        help_text='Select the routine performed during this session.')

    date = models.DateField(
        validators=[validate_not_in_future],
        verbose_name='Workout Date',
        help_text='Select the date when the workout took place.'

    )

    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(
            limit_value=1,
            message='Workout duration must be at least 1 minute.'
        ),

        MaxValueValidator(
            limit_value=1440,
            message='Workout duration cannot exceed 1,440 minutes (24 hours).')],
        verbose_name='Duration (Minutes)',
        help_text='Enter the total duration of the workout in minutes.'
    )

    notes = models.TextField(
        blank=True,
        verbose_name='Notes',
        help_text='Optional notes, performance tracking, or comments about the session.'
    )

    class Meta:
        ordering = ['-date']
        verbose_name = 'Workout Session'
        verbose_name_plural = 'Workout Sessions'

    def __str__(self):
        return f"{self.routine.name} on {self.date}"
