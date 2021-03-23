from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randomsoru/<int:randomsoru>', views.randomsoru, name='randomsoru'),
]
