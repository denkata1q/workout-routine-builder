from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import RoutineForm
from .models import Routine

class RoutineListView(ListView):
    model = Routine
    context_object_name = "routines"
    paginate_by = 9
    def get_queryset(self):
        queryset = Routine.objects.prefetch_related('exercises')
        goal_param= self.request.GET.get('goal')
        if goal_param in Routine.Goal.values:
            queryset = queryset.filter(goal=goal_param)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["goals"] = Routine.Goal.choices
        context["selected_goal"] = self.request.GET.get("goal", "")
        return context

class RoutineCreateView(CreateView):
    model = Routine
    form_class = RoutineForm

class RoutineDetailView(DetailView):
    model = Routine
    context_object_name = "routine"

class RoutineUpdateView(UpdateView):
    model = Routine
    form_class = RoutineForm

class RoutineDeleteView(DeleteView):
    model = Routine
    success_url = reverse_lazy("routine-list")


