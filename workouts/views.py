from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import WorkoutSessionForm
from .models import WorkoutSession

class WorkoutSessionListView(ListView):
    model = WorkoutSession
    context_object_name = "workout_sessions"
    paginate_by = 9

    def get_queryset(self):
        queryset = WorkoutSession.objects.select_related("routine")

        sort_map = {
            "date": "date",
            "-date": "-date",
            "duration": "duration_minutes",
            "-duration": "-duration_minutes",
        }
        sort_param = self.request.GET.get("sort")
        if sort_param in sort_map:
            queryset = queryset.order_by(sort_map[sort_param])

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_sort"] = self.request.GET.get("sort", '')
        return context
class WorkoutSessionCreateView(CreateView):
    model = WorkoutSession
    form_class = WorkoutSessionForm
    success_url = reverse_lazy("workout-list")
