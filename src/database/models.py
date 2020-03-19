import datetime
from peewee import *


db = MySQLDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class BotUser(BaseModel):
    chat_id = CharField(unique=True)
    date_register = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def add(cls, chat_id):
        cls.create(chat_id=chat_id)


class WorldData(BaseModel):
    total_cases = CharField()
    total_recovered = CharField()
    total_unresolved = CharField()
    total_deaths = CharField()
    total_new_cases_today = CharField()
    total_new_deaths_today = CharField()
    total_active_cases = CharField()
    total_serious_cases = CharField()
    date_info = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def add(cls, data):
        cls.create(
            total_cases = data['total_cases'],
            total_recovered = data['total_recovered'],
            total_unresolved = data['total_unresolved'],
            total_deaths = data['total_deaths'],
            total_new_cases_today = data['total_new_cases_today'],
            total_new_deaths_today = data['total_new_deaths_today'],
            total_active_cases = data['total_active_cases'],
            total_serious_cases = data['total_serious_cases']
        )


class BrazilData(BaseModel):
    total_cases = CharField()
    total_recovered = CharField()
    total_unresolved = CharField()
    total_deaths = CharField()
    total_new_cases_today = CharField()
    total_new_deaths_today = CharField()
    total_active_cases = CharField()
    total_serious_cases = CharField()
    date_info = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def add(cls, data):
        cls.create(
            total_cases = data['total_cases'],
            total_recovered = data['total_recovered'],
            total_unresolved = data['total_unresolved'],
            total_deaths = data['total_deaths'],
            total_new_cases_today = data['total_new_cases_today'],
            total_new_deaths_today = data['total_new_deaths_today'],
            total_active_cases = data['total_active_cases'],
            total_serious_cases = data['total_serious_cases']
        )
