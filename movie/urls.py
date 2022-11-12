from django.urls import path

from movie import views

app_name = "movie"
urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movie-list"),
]