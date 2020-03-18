from .models import *
from .db_conn import db

def get_global_news():
    pass

def get_local_news():
    pass

def add_user(chat_id):
    BotUser.add(chat_id)
    db.close()

def save_global_news(data):
    WorldData.add(data)
    db.close()

def save_local_news(data):
    BrazilData.add(data)
    db.close()

def get_users():
    data = [user.chat_id for user in BotUser.select()]
    db.close()
    return data
