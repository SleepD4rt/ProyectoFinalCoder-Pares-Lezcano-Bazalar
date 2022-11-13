from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from movie.models import Movie
from movie.forms import MovieForm


class MovieListView(ListView):
    model = Movie
    paginate_by = 6

class MovieDetailView(DetailView):
    model = Movie
    fields = ["name", "release_date", "produced_by", "description"]

#LoginRequiredMixin
class MovieCreateView(CreateView):
    
    model = Movie
    success_url = reverse_lazy("movie:movie-list")

    form_class = MovieForm

    def form_valid(self, form):
        """Filter to avoid duplicate movies"""
        data = form.cleaned_data
        actual_objects = Movie.objects.filter(
            name=data["name"],
            release_date=data["release_date"],
            produced_by=data["produced_by"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La Movie {data['name']} {data['release_date']} | {data['produced_by']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Movie: {data['name']} - {data['release_date']} | {data['produced_by']}. Creado exitosamente!",
            )
            return super().form_valid(form)

#LoginRequiredMixin
class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["name", "release_date", "produced_by", "description"]

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("movie:movie-detail", kwargs={"pk": movie_id})

#LoginRequiredMixin
class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")
