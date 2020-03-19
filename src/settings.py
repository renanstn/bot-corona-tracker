import os
from dotenv import load_dotenv


load_dotenv()

DATABASE = os.getenv('DATABASE'),
USER = os.getenv('USER'),
PASSWORD = os.getenv('PASS'),
HOST = os.getenv('HOST'),
PORT = os.getenv('PORT')
TOKEN = os.getenv('TOKEN')
