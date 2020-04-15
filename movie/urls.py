from django.urls import path, reverse
from . import views

# app_name = 'movie'

urlpatterns = [
    path('index/', views.index),
]
