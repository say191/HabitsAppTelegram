import requests
from config.settings import TELEGRAM_API_KEY


def get_chat_id(telegram_id):
    """Func for getting owner's chat_id.
    We can use sending message via telegram bot only with chat_id (not @namechannel).
    After user's interaction with telegram bot (pressing button start in bot) we can get chat id
    using method named getUpdates from telegram api bot documentation."""
    token = TELEGRAM_API_KEY
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url).json()

    if len(response['result']) > 0:
        for i in response['result']:
            if 'message' in i.keys():
                if 'chat' in i['message'].keys():
                    if 'username' in i['message']['chat'].keys():
                        if i['message']['chat']['username'] == telegram_id[1:]:
                            return i['message']['chat']['id']
