from bot import Bot
from api import Api
from database.functions import *


def main():
    # Coletar as informações e salvar
    api = Api()
    global_stats = api.get_global_stats()
    save_global_news(global_stats)
    country_stats = api.get_country_stats()
    save_local_news(country_stats)

    # Transmitir as informações
    bot = Bot()
    bot.send_report(global_stats, country_stats)


if __name__ == "__main__":
    main()
