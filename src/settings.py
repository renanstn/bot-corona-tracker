import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')
HOST = os.getenv('DATABASE_URL')
PORT = os.getenv('PORT')
