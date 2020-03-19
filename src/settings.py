import os
from urllib.parse import urlparse
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

# DATABASE_URL = urlparse(os.getenv('DATABASE_URL'))

DATABASE = os.getenv('DATABASE'),
USER = os.getenv('USER'),
PASSWORD = os.getenv('PASS'),
HOST = os.getenv('DATABASE_URL'),
PORT = os.getenv('PORT')
TOKEN = os.getenv('TOKEN')
