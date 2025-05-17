from django.shortcuts import render,HttpResponse
# from telegramapi.management.commands.telegram_userbot import userdetails
from asgiref.sync import async_to_sync
# Create your views here.
def username_details(request,user_id):
    # if request.method == "GET":
    #     user_data = async_to_sync(userdetails)(user_id)
    #     return HttpResponse(user_data, content_type='application/json')
    pass