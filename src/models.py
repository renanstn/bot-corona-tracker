from peewee import *
from db_conn import db


class BaseModel(Model):
    class Meta:
        database = db


class WorldData(BaseModel):
    total_cases = CharField()
    total_recovered = CharField()
    total_unresolved = CharField()
    total_deaths = CharField()
    total_new_cases_today = CharField()
    total_new_deaths_today = CharField()
    total_active_cases = CharField()
    total_serious_cases = CharField()


class BrazilData(BaseModel):
    total_cases = CharField()
    total_recovered = CharField()
    total_unresolved = CharField()
    total_deaths = CharField()
    total_new_cases_today = CharField()
    total_new_deaths_today = CharField()
    total_active_cases = CharField()
    total_serious_cases = CharField()
