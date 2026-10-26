from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse
from exercises.models import Exercise


class Routine(models.Model):

    class Goal(models.TextChoices):
        STRENGTH = "STRENGTH", "Strength"
        ENDURANCE = "ENDURANCE", "Endurance"
        FAT_LOSS = "FAT_LOSS", "Fat Loss"

    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                limit_value=3,
                message="Routine name must be at least 3 characters long."
            ),
        ],
        verbose_name='Routine Name',
        help_text='Enter the name of the routine.'
    )
    goal = models.CharField(
        max_length=20,
        choices=Goal,
        default=Goal.STRENGTH,
        verbose_name="Goal",
        help_text="Select the primary fitness goal of the routine.",
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        help_text='Enter a short description of the routine.'
    )
    exercises = models.ManyToManyField(
        Exercise,
        related_name='routines',
        verbose_name='Exercise',
        help_text='Select the exercises included in this routine.'
    )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created on')

    class Meta:
        ordering = ['-created_on']
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='unique_routine_name_case_insensitive',
                violation_error_message='A routine with this name already exists.'
            )
        ]
        verbose_name = 'Routine'
        verbose_name_plural = 'Routines'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('routine-detail', kwargs={'pk': self.pk})
