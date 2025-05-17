from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_alert(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))