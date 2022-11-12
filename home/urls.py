from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import reverse_lazy


from home import views



app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    ]

