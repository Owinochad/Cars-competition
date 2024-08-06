from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login_user/', views.login_user, name='login-user'),
    path('logout_user/', views.logout_user, name='logout-user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('competitions/', views.competitions, name='competitions'),
    path('competition/<int:competition_id>/', views.competition_details, name='competition'),
    path('competition/<int:id>/add_to_basket/', views.add_to_basket, name='add_to_basket'),
    path('basket/', views.view_basket, name='view_basket'),
]