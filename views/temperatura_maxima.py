from flask import jsonify
from sqlalchemy import func
from datetime import datetime, date
from models.previsao import Previsao, db

def configure(app):
    '''
    /temperatura-maxima - retorna a cidade com a temperatura maxima
    - inicio (YYYY-MM-DD)
    - fim (YYYY-MM-DD)
    '''
    @app.route('/temperatura-maxima/<inicio>/<fim>', methods=['GET'])
    def temperaturaMaxima(inicio, fim):
        try:
            # convertendo os parametros em datetime
            inicio =  datetime.strptime(inicio,'%Y-%m-%d')
            fim =  datetime.strptime(fim,'%Y-%m-%d')

            # buscando a temperatura maxima
            tempMax = db.session.query(Previsao.cidade, Previsao.date, func.max(Previsao.temperatura_max).label('temp')).\
                        filter(Previsao.date >= date(inicio.year, inicio.month, inicio.day)).\
                        filter(Previsao.date <= date(fim.year, fim.month, fim.day)).\
                        first()
            
            # tratando o retorno
            if tempMax is None:
                return jsonify({ 'error': 'O banco de dados está vazio.' })
            else:
                return jsonify({ 'cidade': tempMax.cidade, 'data': str(tempMax.date), 'temperatura' : tempMax.temp })
        except KeyError as e:
            return jsonify({'error': 'O paramêtro "'+str(e)+'" não foi enviado.'})
        except Exception as e:
            return jsonify({'error': str(e)})