from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('distress/', views.create_signal, name="distress")
]