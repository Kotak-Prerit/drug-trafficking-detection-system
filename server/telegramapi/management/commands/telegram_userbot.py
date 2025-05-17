from django.core.management.base import BaseCommand
from telethon import TelegramClient, events
import re,json,os
from django.db.utils import IntegrityError
from DTDS import settings
from suspicous import check_suspicious_patterns
from asgiref.sync import sync_to_async
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import DocumentAttributeVideo
from telethon.tl.types import User, Channel
from telegramapi.models import DetectedMessage,TelegramUser  # Import your models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from check import predict_sentiment

# from myapp.views import notify_new_message  # Import your notify function

# Your API ID and Hash from https://my.telegram.org
api_id = "20018947"
api_hash = "18f9db5fe1125058d5db99181d220d95"
phone_number = "+919998857921"

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Keywords related to drug trafficking
drug_keywords = [
    "drug", "cocaine", "heroin", "weed", "marijuana", "lsd",
    "mdma", "ecstasy", "meth", "narcotics", "substance", "buy", "sell"
]

# Regex pattern to detect suspicious messages
pattern = re.compile(r'\b(?:' + '|'.join(drug_keywords) + r')\b', re.IGNORECASE)
async def download_user_profile_media(user_id, limit=1):
    # Fetch the user profile photos/media
    media_files = await client.get_profile_photos(user_id, limit=limit)

    # If no media is found, print a message
    if not media_files:
        print(f"No media found for user ID {user_id}.")
        return

    # Create a folder to store the downloaded media
    if not os.path.exists('profile_media'):
        os.mkdir('profile_media')

    # Download the media files (image, video, or gif)
    for i, media in enumerate(media_files):
        # print(media.video_sizes())
        media_type = "unknown"
        file_extension = "jpg"  # default for images

        # Check if it's a photo
        if media.video_sizes:
            media_type = "video"
            file_extension = "mp4"
        else:
            media_type = "image"
            file_extension = "jpg"

        # Construct the file path based on the media type
        file_path = f'profile_media/user_{user_id}_media_{i + 1}.{file_extension}'
        file_path=os.path.join(settings.MEDIA_ROOT,file_path)

        # Download and save the media
        await client.download_media(media, file_path)
        return file_path

async def log_message_details(message,detected_by="Pattern"):
    sender = await message.get_sender()
    chat = await message.get_chat()
    print(sender)
    # Check if the sender is a User or a Channel
    if isinstance(sender, User):
        sender_name = f"{sender.first_name} {sender.last_name}" if sender.first_name and sender.last_name else sender.first_name
        telegramuser=TelegramUser(
            user_id=sender.id,
            first_name=sender.first_name,
            last_name=sender.last_name,
            username=sender.username,
            phone_number=sender.phone,
            is_bot=sender.bot,
        )
        file=await download_user_profile_media(sender.id)
        if file:
            telegramuser.photo=file
        try:
            await sync_to_async(telegramuser.save)()
        except IntegrityError:
            print("TelegramUser already exists")
    elif isinstance(sender, Channel):
        sender_name = sender.title  # For Channels, use the channel title as the name
    else:
        sender_name = None  # If no sender info is available
    # Save the message details to the database and notify via WebSocket
    detected_message = DetectedMessage(
        message_id=message.id,
        chat_id=chat.id,
        chat_name=chat.title if chat.title else chat.username,
        sender_id=sender.id if sender != None else None,
        sender_name=sender_name,
        sender_username=sender.username if sender != None else None,
        text=message.text,
        date=message.date,
        message_link=f"https://t.me/{chat.username}/{message.id}" if chat.username else None,
        detected_by=detected_by
    )
    await sync_to_async(detected_message.save)()
    channel_layer = get_channel_layer()
    if channel_layer is None:
        print("❌ Channel Layer is not initialized!")
    else:
        async_to_sync(channel_layer.group_send)(
        "alerts",
        {
            "type": "send.alert",
            "message": f"Drug-related message detected: {message}"
        }
        )
        print("Message details logged and notified")
    # notify_new_message({
    #     "message_id": detected_message.message_id,
    #     "chat_id": detected_message.chat_id,
    #     "chat_name": detected_message.chat_name,
    #     "sender_id": detected_message.sender_id,
    #     "sender_name": detected_message.sender_name,
    #     "sender_username": detected_message.sender_username,
    #     "text": detected_message.text,
    #     "date": detected_message.date.isoformat(),
    #     "message_link": detected_message.message_link,
    # })

@client.on(events.NewMessage)
async def handler(event):
    if check_suspicious_patterns(event.message.message):
        await log_message_details(event.message)
    if predict_sentiment(event.message.message)=="positive":
        await log_message_details(event.message,detected_by="AI")
class Command(BaseCommand):
    help = 'Run the Telethon bot'

    def handle(self, *args, **kwargs):
        import asyncio
        loop = asyncio.get_event_loop()
        client.start(phone=phone_number)
        loop.run_until_complete(client.run_until_disconnected())
