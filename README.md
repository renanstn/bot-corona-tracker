# Corona Tracker

A idéia deste app é fazer um bot do telegram que de hora em hora entregue informações atualizadas sobre a situação do corona vírus no mundo.

Este app utiliza como fonte de dados [esta API](https://thevirustracker.com/api)

## Desenvolvimento sem Docker
- Clone o projeto
- Instale as dependências
    - `pipenv install`
- Inicialize um shell
    - `pipenv shell`
- Inicialize as models (necessário somente uma vez)
    - `cd src`
    - `python int_db.py`
- Ligar o bot para receber usuarios
    - `python listen.py`
- Script chamado via cron para coletar e enviar as informações para os usuários registrados
    - `python check_news.py`

## Desenvolvimento com Docker
- Subir ambiente
    - `docker-compose up -d`
- Inicializar banco de dados (necessário somente pela primeira vez)
    - `docker-compose run bot python init_db.py`
