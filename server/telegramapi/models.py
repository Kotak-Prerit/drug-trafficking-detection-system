# Create your models here.
from django.db import models

class DetectedMessage(models.Model):
    AI_CHOICES = [
        ('AI', 'AI'),
        ('Pattern', 'Pattern'),
        # ('BERT', 'BERT'),
        # ('Other', 'Other'),
    ] 
    message_id = models.BigIntegerField()
    chat_id = models.BigIntegerField()
    chat_name = models.CharField(max_length=255, null=True, blank=True)
    sender_id = models.BigIntegerField()
    sender_name = models.CharField(max_length=255, null=True, blank=True)
    sender_username = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField()
    message_link = models.URLField(null=True, blank=True)
    detected_by = models.CharField(max_length=50, choices=AI_CHOICES, default='Pattern')
    def __str__(self):
        return f"{self.detected_by} - {self.text[:50]}... Message {self.message_id} from {self.sender_name} in {self.chat_name}"

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    photo= models.FileField(upload_to='profile_media',blank=True, null=True)
    is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.username if self.username else f"{self.first_name} {self.last_name}"
