import requests

class Api:
    '''
    Classe que faz a comunicação com a API do Virustracker
    '''
    URL_GLOBAL_STATS = 'https://thevirustracker.com/free-api?global=stats'
    URL_COUNTRY_BR = 'https://thevirustracker.com/free-api?countryTotal=BR'

    def get_global_stats(self):
        data = requests.get(self.URL_GLOBAL_STATS).json()
        return data

    def get_country_stats(self):
        data = requests.get(self.URL_COUNTRY_BR).json()
        return data['countrydata']
