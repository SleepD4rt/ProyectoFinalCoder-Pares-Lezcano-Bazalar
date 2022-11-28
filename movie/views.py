from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from movie.models import Movie
from movie.forms import MovieForm


class MovieListView(ListView):
    model = Movie
    paginate_by = 2


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"
    fields = ["name", "release_date", "director", "description", "image", "studio", "duration", "rating"] 


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
            studio=data["studio"],
                    ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La Pelicula {data['name']} de {data['studio']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"La pelicula {data['name']} de {data['studio']}. Creado exitosamente!",
            )
            return super().form_valid(form)

#LoginRequiredMixin
class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["name", "release_date", "director", "description", "image", "studio", "duration", "rating"] 

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("movie:movie-detail", kwargs={"pk": movie_id})

#LoginRequiredMixin
class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movie:movie-list")

#Buscador
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        movies = Movie.objects.filter(query)
        context_dict.update(
            {
                "movies": movies,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="movie/movie_search.html",
    )
