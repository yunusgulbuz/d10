from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:randomsoru>', views.index, name='randomsoru'),
]
