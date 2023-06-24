from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    # equivalent of localhost:8000/
]
