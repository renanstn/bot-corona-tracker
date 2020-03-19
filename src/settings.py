import os
from urllib.parse import urlparse
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

url = urlparse(os.getenv('DATABASE_URL'))

DATABASE = url.path
USER = url.username
PASSWORD = url.password
HOST = url.hostname
PORT = url.port
TOKEN = os.getenv('TOKEN')

# DATABASE = os.getenv('DATABASE'),
# USER = os.getenv('USER'),
# PASSWORD = os.getenv('PASS'),
# HOST = os.getenv('DATABASE_URL'),
# PORT = os.getenv('PORT')
# TOKEN = os.getenv('TOKEN')
