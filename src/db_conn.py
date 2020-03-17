from peewee import *
from configparser import ConfigParser


'''
Faz a conexão com o banco de dados postgreSQL
Necessita de um arquivo config.ini com os seguintes parâmetros:
    [db]
    host = 0.0.0.0
    port = 5432
    database = database
    user = user
    pass = pass

'''
parser = ConfigParser()
parser.read('./config.ini')
db_params = parser['db']

db = PostgresqlDatabase(
    db_params['database'],
    user = db_params['user'],
    password = db_params['pass'],
    host = db_params['host'],
    port = db_params['port']
)
