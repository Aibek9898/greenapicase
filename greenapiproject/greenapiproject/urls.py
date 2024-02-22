from django.urls import path
from greenapi import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_data/', views.get_data, name='get_data'),
    path('send_message/', views.send_message, name='send_message'),
    path('send_file/', views.send_file, name='send_file'),
]