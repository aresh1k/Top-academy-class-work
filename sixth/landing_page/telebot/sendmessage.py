import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=2):
        settings = TeleSettings.objects.get(pk=2)
        token = settings.tg_token
        chat_id = settings.tg_chat
        text = settings.tg_message

        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part1 = text[:text.find('{')]
            part2 = text[text.find('}') + 1:text.rfind('{')]

            text_slice = part1 + tg_name + part2 + tg_phone
        else:
            text_slice = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice,
            })
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка сервера')
            else:
                print('Сообщение отправлено успешно')
