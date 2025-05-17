from rest_framework import serializers
from telegramapi.models import DetectedMessage,TelegramUser

class DetectedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectedMessage
        fields = '__all__'
class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'