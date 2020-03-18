# Corona Tracker

A idéia deste app é fazer um bot do telegram que de hora em hora entregue informações atualizadas sobre a situação do corona vírus no mundo.

Este app utiliza como fonte de dados [esta API](https://thevirustracker.com/api)

Link para o bot: https://t.me/CoronaReportsBot

Basta dar ao bot o comando `/register` para começar a receber avisos.

<img src="https://github.com/Doc-McCoy/bot-corona-tracker/blob/master/screenshots/01.jpg" width="360" height="640"/>

## Desenvolvimento com Docker

- Subir ambiente
    - `docker-compose up -d`
- Inicializar banco de dados (necessário somente pela primeira vez)
    - `docker-compose run --rm bot python init_db.py`
- Executar manualmente a verificação de novos números
    - `docker-compose run --rm bot python check_news.py`


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

## config.ini

- Em ambos os casos, é necessário criar um arquivo `config.ini` dentro da pasta `src` com a seguinte estrutura:

```ini
[db]
host = <host>
port = <port>
database = <database>
user = <user>
pass = <password>

[telegram]
token = <token_do_telegram>
```
