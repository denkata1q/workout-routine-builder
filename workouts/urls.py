from django.urls import path
from . import views

urlpatterns = [
    path("", views.WorkoutSessionListView.as_view(), name="workout-list"),
    path("create/", views.WorkoutSessionCreateView.as_view(), name="workout-create"),
]
