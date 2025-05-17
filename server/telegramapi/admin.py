from django.contrib import admin
from .models import DetectedMessage,TelegramUser
# Register your models here.
admin.site.register(DetectedMessage)
admin.site.register(TelegramUser)