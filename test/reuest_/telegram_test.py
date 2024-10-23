import requests

TELEGRAM_BOT_TOKEN = '6478297122:AAFh71qR8bIh-9vmN6NAwZZa2UoVCKFtKUY'
CHAT_ID = '-1002178377754'

def send_message_to_shat_id(text: str='') -> None:
    """ Отправляет сообщение в чат с телеграм ботом"""
    api = 'https://api.telegram.org/bot'
    method = api + TELEGRAM_BOT_TOKEN + '/sendMessage'

    req = requests.post(method,
                        data={
                            'chat_id': CHAT_ID,
                            'text': text
                        })

send_message_to_shat_id('тест')
