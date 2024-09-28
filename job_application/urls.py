from django.urls import path
from . import views

urlpatterns = [
    # the homepage should be connected to this file
    path('', views.index, name="index"),
    path('about/', views.about, name="about")
]