from django.urls import path

from movie import views

app_name = "movie"
urlpatterns = [
    path("movie/", views.MovieListView.as_view(), name="movie-list"),
]