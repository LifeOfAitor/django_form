from django.urls import path
from . import views

urlpatterns = [
    # the homepage should be connected to this file
    path('', views.index, name="index")
]