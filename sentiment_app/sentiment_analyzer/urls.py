from django.urls import path
from . import views

urlpatterns = [
    path("sentiment/", views.sentiment_analysis, name="sentiment_analysis"),
    path("image/", views.image_classification, name="image_classification")
]