import os
import settings
from sys import argv
from database.models import db
from check_news import check
from listen import listen
from functions.init_db import init_db


OPTIONS = ['init', 'listen', 'check_news']

# Inicializar o banco
db.init(
    settings.DATABASE,
    user = settings.USER,
    password = settings.PASSWORD,
    host = settings.HOST,
    port = settings.PORT
)

if len(argv) > 1 and argv[1] in OPTIONS:
    arg = argv[1]

    if arg == 'init':
        init_db()

    if arg == 'check_news':
        check()

    if arg == 'listen':
        listen()

else:
    print(
        'Necessário passar um dos argumentos: '
        'init | listen | check_news'
    )
