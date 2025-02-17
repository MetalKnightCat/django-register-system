from django.urls import path
from app_register import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_list/', views.user_list, name='user_list'),
]