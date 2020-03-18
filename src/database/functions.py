from .models import *

def get_global_news():
    pass

def get_local_news():
    pass

def add_user(chat_id):
    BotUser.add(chat_id)

def save_global_news(data):
    WorldData.add(data)

def save_local_news(data):
    BrazilData.add(data)

def get_users():
    return [user.chat_id for user in BotUser.select()]
