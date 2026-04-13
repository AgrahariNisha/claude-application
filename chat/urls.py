from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('chat/<int:session_id>/', views.chat_session, name='chat_session'),
    path('send/<int:session_id>/', views.send_message, name='send_message'),
    path('new/', views.new_chat, name='new_chat'),
    path('clear/<int:session_id>/', views.clear_messages, name='clear_messages'),
]