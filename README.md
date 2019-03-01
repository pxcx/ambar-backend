Este projeto foi criado com [Flask](http://flask.pocoo.org/) :heart: para o teste técnico da Ambar.

## Dependências

Para executar o projeto as seguintes libs são necessárias:

certifi==2018.11.29
chardet==3.0.4
Click==7.0
Flask==1.0.2
Flask-API==1.1
Flask-Cors==3.0.7
Flask-SQLAlchemy==2.3.2
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.1
pkg-resources==0.0.0
requests==2.21.0
six==1.12.0
SQLAlchemy==1.2.18
urllib3==1.24.1
Werkzeug==0.14.1

Você pode executar o seguinte comando no diretório do projeto para instalar as libs:

### `pip install -r requirements.txt`

Para executar o servidor de desenvolvimento da API:

### `pyhton app.py`

O servidor de desenvolvimento iniciará na URL: [http://localhost:5000](http://localhost:5000).

## Endpoints

Para cumprir as exigências do teste os seguintes endpoints foram criados:

### `[POST] /coleta`
Faz a coleta dos dados da cidade informada como parametro.

Parâmetros:

- cidade (string)
- uf (string)

### `[GET] /temperatura-maxima/<inicio>/<fim>`
Retorna a cidade com a temperatura maxima.

Parâmetros:

- inicio (string: YYYY-MM-DD)
- fim (string: YYYY-MM-DD)

### `[GET] /precipitacao/<inicio>/<fim>`
Retorna uma lista de média de precipitacao por cidade.

Parâmetros:

- inicio (string: YYYY-MM-DD)
- fim (string: YYYY-MM-DD)

### `[GET] /probabilidade/<inicio>/<fim>`
Retorna a probabilidade total de chuva.

Parâmetros:

- inicio (string: YYYY-MM-DD)
- fim (string: YYYY-MM-DD)
