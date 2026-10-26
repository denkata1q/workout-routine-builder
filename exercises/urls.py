from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExerciseListView.as_view(), name="exercise-list"),
    path("create/", views.ExerciseCreateView.as_view(), name="exercise-create"),
    path("<int:pk>/", views.ExerciseDetailView.as_view(), name="exercise-detail"),
    path("<int:pk>/update/", views.ExerciseUpdateView.as_view(), name="exercise-update"),
    path("<int:pk>/delete/", views.ExerciseDeleteView.as_view(), name="exercise-delete"),
    path("musclegroups/", views.MuscleGroupListView.as_view(), name="musclegroup-list"),
    path("musclegroups/create/", views.MuscleGroupCreateView.as_view(), name="musclegroup-create"),
]