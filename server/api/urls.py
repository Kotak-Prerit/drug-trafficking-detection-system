from django.urls import path
from .views import *
urlpatterns = [
    path('detected-message', get_messages, name='get_messages'),
    path('telegram-users', get_tusers, name='get_tusers'),
    path('username_details', userdetails, name='get_tusers'),
]
