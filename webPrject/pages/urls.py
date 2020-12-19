from django.urls import path,include
from . import views

urlpatterns = [
    path('formm', views.form_map_to_model),
    path('index', views.index),
    path('playing', views.playing),
    path('written', views.written),
    path('reading', views.reading),
    path('', include('product.urls')),

]
