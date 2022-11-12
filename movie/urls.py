from django.urls import path

from movie import views

app_name = "movie"
urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movie-list"),
    path("movie/add/", views.MovieCreateView.as_view(), name="movie-add"),

]