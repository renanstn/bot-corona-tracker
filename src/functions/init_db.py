import os
from peewee import *
from database.models import *


def init_db():
    '''
    Cria as tabelas iniciais necessárias
    '''
    db.create_tables([BotUser, WorldData, BrazilData])
    db.close()
