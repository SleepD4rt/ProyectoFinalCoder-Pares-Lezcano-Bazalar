from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import reverse_lazy

from home import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path("register/", views.register, name="user-register"),
    #path('register/update/', views.user_update, name='user-update'),

    ]

