import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone, tg_email, tg_time, tg_people):
    settings = TeleSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_message
    api = "https://api.telegram.org/bot"
    method = api + token + "/sendMessage"

    if text.find('{') != -1 and text.find('}') != -1:
        part_1 = text[:text.find('{')]
        part_2 = text[text.find('}') + 1:text.find('{', text.find('}') + 1)]
        part_3 = text[text.find('}', text.find('}') + 1) + 1:text.find('{', text.find('}', text.find('}') + 1) + 1)]
        part_4 = text[text.find('}', text.find('}', text.find('}') + 1) + 1) + 1:text.find('{', text.find('}',
                                                                                                          text.find('}',
                                                                                                                    text.find(
                                                                                                                        '}') + 1) + 1) + 1)]
        part_5 = text[text.find('}', text.find('}', text.find('}', text.find('}') + 1) + 1) + 1) + 1:text.rfind('{')]
        part_6 = text[text.rfind('}') + 1:]
        text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_email + part_4 + str(tg_time) + part_5 + str(
            tg_people) + part_6
    else:
        text_slice = text

    requests.post(method, data={
        "chat_id": chat_id,
        'text': text_slice,
    })
