
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about.html', views.about),
    path('Elite_Weather.html', views.Elite_Weather),
]
