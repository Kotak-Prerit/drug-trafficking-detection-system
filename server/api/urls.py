from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'detectedmessage', DetectedMessageViewSet, basename='detectedmessage')
router.register(r'telegramusers', TelegramUserViewSet, basename='telegramusers')

urlpatterns = [
    # path('detected-message', get_messages, name='get_messages'),
    # path('telegram-users', get_tusers, name='get_tusers'),
    path('username_details', userdetails, name='get_tusers'),
    path('', include(router.urls), name='get_tuser'),
]
