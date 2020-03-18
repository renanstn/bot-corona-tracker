from .models import *


def add_user(chat_id):
    BotUser.add(chat_id)

def save_global_news(data):
    WorldData.add(data)

def save_local_news(data):
    BrazilData.add(data)
