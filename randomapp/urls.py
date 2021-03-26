from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:randomsoru>', views.index, name='randomsoru'),
    path('mufredat/', views.mufredat, name='mufredat'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
