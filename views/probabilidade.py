from flask import jsonify
from sqlalchemy import func
from datetime import datetime, date
from models.previsao import Previsao, db

def configure(app):
    '''
    /probabilidade - retorna a probabilidade total de chuva
    - inicio (YYYY-MM-DD)
    - fim (YYYY-MM-DD)
    '''
    @app.route('/probabilidade/<inicio>/<fim>', methods=['GET'])
    def probabilidade(inicio, fim):
        try:
            # convertendo os parametros em datetime
            inicio =  datetime.strptime(inicio,'%Y-%m-%d')
            fim =  datetime.strptime(fim,'%Y-%m-%d')

            # total de cidades cadastradas
            totalCidades = db.session.query(func.count(Previsao.cidade).label('total_cidades')).\
                        filter(Previsao.date >= date(inicio.year, inicio.month, inicio.day)).\
                        filter(Previsao.date <= date(fim.year, fim.month, fim.day)).\
                        group_by(Previsao.cidade).\
                        first()
            totalCidades = totalCidades.total_cidades

            # buscando a probabilidade de chuva por dia
            probabilidadeList = db.session.query(Previsao.date, Previsao.chuva_probabilidade).\
                        filter(Previsao.date >= date(inicio.year, inicio.month, inicio.day)).\
                        filter(Previsao.date <= date(fim.year, fim.month, fim.day)).\
                        all()
            
            #formatando a saida
            pa = 1/totalCidades

            aux = {}
            for i in probabilidadeList:
                pb = i.chuva_probabilidade/100
                if str(i.date) in aux:
                    aux[str(i.date)] = aux[str(i.date)] + pb*(pb*pa)/pa
                else:
                    aux[str(i.date)] = pb*(pb*pa)/pa

            out = 0
            for key,val in aux.items():
                if out > 0:
                    out = out + val*(val*pa)/pa
                else:
                    out = val*(val*pa)/pa

            return jsonify({'probabilidade_chuva': out})

        except KeyError as e:
            return jsonify({'error': 'O paramêtro "'+str(e)+'" não foi enviado.'})
        except Exception as e:
            return jsonify({'error': str(e)})

    if __name__ == "__main__":
        app.run(debug=True)