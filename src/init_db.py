from peewee import *
from models import *


'''
Cria as tabelas iniciais necessárias
'''
db.create_tables([WorldData, BrazilData])
db.close()
