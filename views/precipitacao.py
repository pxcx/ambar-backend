from flask import jsonify
from sqlalchemy import func
from datetime import datetime, date
from models.previsao import Previsao, db

def configure(app):
    '''
    rota: /precipitacao - retorna uma lista de média de precipitacao por cidade
    - inicio (YYYY-MM-DD)
    - fim (YYYY-MM-DD)
    '''
    @app.route('/precipitacao/<inicio>/<fim>', methods=['GET'])
    def precipitacao(inicio, fim):
        try:
            # convertendo os parametros em datetime
            inicio =  datetime.strptime(inicio,'%Y-%m-%d')
            fim =  datetime.strptime(fim,'%Y-%m-%d')

            # buscando a media de precipitacao por cidade
            precipitacaoList = db.session.query(Previsao.cidade,  func.avg(Previsao.chuva_precipitacao).label('precipitacao')).\
                        filter(Previsao.date >= date(inicio.year, inicio.month, inicio.day)).\
                        filter(Previsao.date <= date(fim.year, fim.month, fim.day)).\
                        group_by(Previsao.cidade).\
                        all()
            
            #formatando a saida
            out = []
            for i in precipitacaoList:
                out.append({'cidade':i.cidade, 'precipitacao':i.precipitacao})

            return jsonify(out)

        except KeyError as e:
            return jsonify({'error': 'O paramêtro "'+str(e)+'" não foi enviado.'})
        except Exception as e:
            return jsonify({'error': str(e)})