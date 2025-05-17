from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('username_details/<int:user_id>', username_details, name='username_details'),
]
