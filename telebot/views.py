import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TelegramUser
from decouple import config

# You can also put BOT_TOKEN into your .env for better security
BOT_TOKEN = config('BOT_TOKEN')

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message')

        if message:
            chat = message.get('chat')
            text = message.get('text')

            if text == '/start':
                telegram_id = chat.get('id')
                username = chat.get('username')
                first_name = chat.get('first_name')
                last_name = chat.get('last_name')

                TelegramUser.objects.get_or_create(
                    telegram_id=telegram_id,
                    defaults={
                        'username': username,
                        'first_name': first_name,
                        'last_name': last_name,
                    }
                )

                send_message(telegram_id, f"Welcome {first_name}! You are registered.")

        return JsonResponse({'ok': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)