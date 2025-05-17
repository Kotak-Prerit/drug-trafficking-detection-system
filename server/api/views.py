from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from telethon.tl.functions.users import GetFullUserRequest
from telegramapi.models import DetectedMessage,TelegramUser
from .serializers import DetectedMessageSerializer,TelegramUserSerializer
from telethon import TelegramClient, events
from telethon.tl.functions.contacts import ResolveUsernameRequest
import json
from asgiref.sync import async_to_sync
# Your API ID and Hash from https://my.telegram.org
api_id = "20018947"
api_hash = "18f9db5fe1125058d5db99181d220d95"
phone_number = "+919998857921"

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

class DetectedMessageViewSet(viewsets.ModelViewSet):
    queryset = DetectedMessage.objects.all()
    serializer_class = DetectedMessageSerializer

@api_view(['GET'])
def userdetails(request):
    user_id = request.GET.get("user_id")  # Get user_id from query parameters
    username = request.GET.get("username")  # Get username if provided

    if not user_id and not username:
        return Response({"error": "Either user_id or username parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Ensure the client is connected before making a request
        async_to_sync(client.connect)()

        if not async_to_sync(client.is_user_authorized)():
            return Response({"error": "Telegram client is not authorized. Please log in."}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch user details based on user_id or username
        if username:
            result = async_to_sync(client)(ResolveUsernameRequest(username))
            user_id = result.users[0].id  # Get user ID from username lookup

        user_full = async_to_sync(client)(GetFullUserRequest(int(user_id)))  # Convert user_id to int
        user = user_full.users[0]  # Extract user object

        user_info = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "bio": user_full.full_user.about if user_full.full_user else None,
            "is_bot": user.bot,
            "is_premium": user.premium if hasattr(user, "premium") else False,
            "restricted": user.restricted,
            "scam": user.scam,
            "verified": user.verified,
            "status": str(user.status) if hasattr(user, "status") else "Unknown",
            "profile_photo": user_full.full_user.profile_photo.photo_id if user_full.full_user.profile_photo else None,
        }

        return Response(user_info, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    finally:
        async_to_sync(client.disconnect)()
        
class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer