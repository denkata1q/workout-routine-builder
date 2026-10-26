from django.urls import path
from . import views

urlpatterns = [
    path("", views.RoutineListView.as_view(), name="routine-list"),
    path("create/", views.RoutineCreateView.as_view(), name="routine-create"),
    path("<int:pk>/", views.RoutineDetailView.as_view(), name="routine-detail"),
    path("<int:pk>/update/", views.RoutineUpdateView.as_view(), name="routine-update"),
    path("<int:pk>/delete/", views.RoutineDeleteView.as_view(), name="routine-delete"),
]