from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index),
    path('playing', views.playing),
    path('written', views.written),
    path('reading', views.reading),
]