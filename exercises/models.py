from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100,verbose_name="Muscle Group Name",
        help_text="Enter a unique name for the muscle group.")
    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_musclegroup_name_case_insensitive",
                violation_error_message="A muscle group with this name already exists.",
            )
        ]
        verbose_name = "Muscle Group"
        verbose_name_plural = "Muscle Groups"

    def __str__(self):
        return self.name


class Exercise(models.Model):

    class Difficulty(models.TextChoices):
        BEGINNER = "BEGINNER", "Beginner"
        INTERMEDIATE = "INTERMEDIATE", "Intermediate"
        ADVANCED = "ADVANCED", "Advanced"

    name = models.CharField(max_length=200,
           validators=[MinLengthValidator(
           limit_value=3,
           message="Exercise name must be at least 3 characters long.")],
           verbose_name = "Exercise Name",
           help_text = "Enter the name of the exercise.",
    )
    description = models.TextField(blank=True,
        verbose_name = "Exercise Description",
        help_text = "Enter a description of the exercise.",)

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty,
        default=Difficulty.BEGINNER,
        verbose_name="Difficulty",
        help_text="Select the difficulty of the exercise.",
    )

    muscle_groups = models.ManyToManyField(MuscleGroup,related_name='exercises',
        verbose_name="Muscle Groups",
        help_text="Select which muscle groups this exercise belongs to.")

    created_on = models.DateTimeField(auto_now_add=True,
        verbose_name="Created on",)

    class Meta:
        ordering = ['-created_on']
        constraints = [models.UniqueConstraint(
            Lower('name'),
            name='unique_exercise_name_case_insensitive',
            violation_error_message="An exercise with this name already exists.",
        )]
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise-detail', kwargs={'pk': self.pk})

    @property
    def muscle_groups_string(self):
        """Returns all trained muscle groups as a comma-joined string."""
        return ", ".join(mg.name for mg in self.muscle_groups.all())
