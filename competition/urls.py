from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login_user/', views.login_user, name='login-user'),
    path('logout_user/', views.logout_user, name='logout-user'),
    path('dashboard/', views.dashboard, name='dashboard'),



]