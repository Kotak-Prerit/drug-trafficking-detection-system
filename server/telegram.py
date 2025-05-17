hash="18f9db5fe1125058d5db99181d220d95"
from telethon import TelegramClient, events
import re
from suspicous import check_suspicious_patterns

# Your API ID and Hash from https://my.telegram.org
api_id="20018947"
api_hash = hash
phone_number = +919998857921

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Keywords related to drug trafficking
drug_keywords = [
    "drug", "cocaine", "heroin", "weed", "marijuana", "lsd",
    "mdma", "ecstasy", "meth", "narcotics", "substance", "buy", "sell"
]

# Regex pattern to detect suspicious messages
pattern = re.compile(r'\b(?:' + '|'.join(drug_keywords) + r')\b', re.IGNORECASE)

async def check_old_messages(chat):
    async for message in client.iter_messages(chat, limit=1000):  # Adjust limit as needed
        if pattern.search(message.text or ''):
            print(f"Suspicious old message detected: {message.text}")
            print(f"Sender: {message.sender_id}")
            print(f"Chat: {message.chat_id}")
async def log_message_details(message):
    sender = await message.get_sender()

    chat = await message.get_chat()
    # print(chat)
    # print(sender)
    print(f"Suspicious message detected: {message.text}")
    print(f"Message ID: {message.id}")
    print(f"Chat ID: {chat.id} (Name: " if chat.title else chat.username ,")")
    print(f"Sender ID: {sender.id} (Name: {sender.first_name} {sender.last_name}, Username: {sender.username})")
    print(f"Date: {message.date}")
    print(f"Message Link: https://t.me/{chat.username}/{message.id}" if chat.username else "No public link available")

@client.on(events.NewMessage)
async def handler(event):
    # print(event.message.message)
    if check_suspicious_patterns(event.message.message):
        await log_message_details(event.message)
    # if pattern.search(event.message.message):
    #     await log_message_details(event.message)

async def main():
    # Start the client
    await client.start(phone=phone_number)
    print("Monitoring started...")

    # Define the group/channel IDs or usernames you want to monitor
    # chats_to_monitor = ['group_username_or_id', 'channel_username_or_id']

    # # Check old messages in the specified groups/channels
    # for chat in chats_to_monitor:
    #     await check_old_messages(chat)

    # Run the client until manually disconnected
    await client.run_until_disconnected()

# Running the main function
with client:
    client.loop.run_until_complete(main())
