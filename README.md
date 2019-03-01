Este projeto foi criado com [Flask](http://flask.pocoo.org/) :heart: para o teste técnico da Ambar.

## Dependências

Para executar o projeto as seguintes libs são necessárias:

certifi==2018.11.29<br>
chardet==3.0.4<br>
Click==7.0<br>
Flask==1.0.2<br>
Flask-API==1.1<br>
Flask-Cors==3.0.7<br>
Flask-SQLAlchemy==2.3.2<br>
idna==2.8<br>
itsdangerous==1.1.0<br>
Jinja2==2.10<br>
MarkupSafe==1.1.1<br>
pkg-resources==0.0.0<br>
requests==2.21.0<br>
six==1.12.0<br>
SQLAlchemy==1.2.18<br>
urllib3==1.24.1<br>
Werkzeug==0.14.1

Você pode executar o seguinte comando no diretório do projeto para instalar as libs:

### `pip install -r requirements.txt`

Para executar o servidor de desenvolvimento da API:

### `pyhton app.py`

O servidor de desenvolvimento iniciará na URL: [http://localhost:5000](http://localhost:5000).

## Endpoints

Para cumprir as exigências do teste os seguintes endpoints foram criados:

#### `[POST] /coleta`
Faz a coleta dos dados da cidade informada como parametro.

Parâmetros:

- cidade (string)
- uf (string)

#### `[GET] /temperatura-maxima/<inicio>/<fim>`
Retorna a cidade com a temperatura maxima.

Parâmetros:

- inicio (string: YYYY-MM-DD)
- fim (string: YYYY-MM-DD)

Exemplo: [http://localhost:5000/temperatura-maxima/2019-03-01/2019-03-05](http://localhost:5000/temperatura-maxima/2019-03-01/2019-03-05)

#### `[GET] /precipitacao/<inicio>/<fim>`
Retorna uma lista de média de precipitacao por cidade.

Parâmetros:

- inicio (string: YYYY-MM-DD)
- fim (string: YYYY-MM-DD)

Exemplo: [http://localhost:5000/precipitacao/2019-03-01/2019-03-05](http://localhost:5000/precipitacao/2019-03-01/2019-03-05)

#### `[GET] /probabilidade/<inicio>/<fim>`
Retorna a probabilidade total de chuva.

Parâmetros:

- inicio (string: YYYY-MM-DD)
- fim (string: YYYY-MM-DD)

Exemplo: [http://localhost:5000/probabilidade/2019-03-01/2019-03-05](http://localhost:5000/probabilidade/2019-03-01/2019-03-05)
