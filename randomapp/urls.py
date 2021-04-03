from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:randomsoru>', views.index, name='randomsoru'),
    path('mufredat/', views.mufredat, name='mufredat'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),

    path('yuzune/<int:randomsoru>', views.yuzune, name='kiraat'),
    path('ezber/<int:randomsoru>', views.ezber, name='ezber'),
    path('tecvid/<int:randomsoru>', views.tecvid, name='tecvid'),
    path('ilmihal_siyer_dua/<int:randomsoru>', views.ilmihal_siyer_dua, name='ilmihal_siyer_dua'),

]
