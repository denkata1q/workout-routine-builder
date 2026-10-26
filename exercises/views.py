from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import ExerciseForm, MuscleGroupForm
from .models import Exercise, MuscleGroup

class ExerciseListView(ListView):
    model = Exercise
    context_object_name = "exercises"
    paginate_by = 9
    def get_queryset(self):
        queryset = Exercise.objects.prefetch_related('muscle_groups')
        muscle_group_id = self.request.GET.get("muscle_group")
        if muscle_group_id:
            queryset = queryset.filter(muscle_groups__pk=muscle_group_id)
        sort_map = {
                "name": "name",
                "-name": "-name",
                "difficulty": "difficulty",
                "-difficulty": "-difficulty",
                "created_on": "-created_on",
            }
        sort_param=self.request.GET.get('sort')
        if sort_param in sort_map:
            queryset = queryset.order_by(sort_map[sort_param])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['muscle_groups'] = MuscleGroup.objects.all()
        return context

class ExerciseDetailView(DetailView):
    model = Exercise
    context_object_name = "exercise"


class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm


class ExerciseUpdateView(UpdateView):
    model = Exercise
    form_class = ExerciseForm


class ExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = reverse_lazy("exercise-list")


class MuscleGroupListView(ListView):
    model = MuscleGroup
    context_object_name = "muscle_groups"


class MuscleGroupCreateView(CreateView):
    model = MuscleGroup
    form_class = MuscleGroupForm
    success_url = reverse_lazy("musclegroup-list")