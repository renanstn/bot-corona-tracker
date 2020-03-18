from peewee import *
from database.models import *


'''
Cria as tabelas iniciais necessárias
'''
db.create_tables([BotUser, WorldData, BrazilData])
db.close()
