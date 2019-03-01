import requests
import json
from flask import jsonify, request
from datetime import datetime, date
from models.previsao import Previsao, db

def configure(app):
    '''
    /coleta - faz a coleta dos dados da cidade informada como parametro
    - cidade (string)
    - uf (string)
    '''
    @app.route('/coleta', methods=['POST'])
    def coleta():
        try:
            param = request.get_json()
            # obtendo o id da cidade
            reqCity = requests.get('http://apiadvisor.climatempo.com.br/api/v1/locale/city?name='+param['cidade']+'&state='+param['uf']+'&token=d9596b26d990306bc6a6fd056dfd1c13')
            city = json.loads(reqCity.text)
            cityId = city[0]['id']
            # obtendo a previsao de 15 dias
            reqPrevisao = requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'+ str(cityId) +'/days/15?token=d9596b26d990306bc6a6fd056dfd1c13')
            previsao = json.loads(reqPrevisao.text)
            # atualizando a base de dados
            for data in previsao['data']:
                # verificando se o registro existe
                prevDate = datetime.strptime(data['date'],'%Y-%m-%d')
                prev = Previsao.query.filter_by(
                    cidade=previsao['name'],
                    uf=previsao['state'],
                    pais=previsao['country'],
                    date=date(prevDate.year, prevDate.month, prevDate.day)
                ).first()
                if prev is None:
                    # nao existe este registro, criando um novo
                    novaPrevisao = Previsao(
                        cidade=previsao['name'],
                        uf=previsao['state'],
                        pais=previsao['country'],
                        date=datetime.strptime(data['date'],'%Y-%m-%d'),
                        chuva_probabilidade=data['rain']['probability'],
                        chuva_precipitacao=data['rain']['precipitation'],
                        temperatura_min=data['temperature']['min'],
                        temperatura_max=data['temperature']['max']
                    )
                    db.session.add(novaPrevisao)
                else:
                    # atualizando o registro
                    prev.chuva_probabilidade = data['rain']['probability']
                    prev.chuva_precipitacao = data['rain']['precipitation']
                    prev.temperatura_min = data['temperature']['min']
                    prev.temperatura_max = data['temperature']['max']
                db.session.commit()
            
            #retornando os dados recem adicionados
            return jsonify(previsoes(previsao['name'], previsao['state'], previsao['country']))
        except KeyError as e:
            return jsonify({'error': 'O paramêtro "'+str(e)+'" não foi enviado.'})
        except Exception as e:
            return jsonify({'error': str(e)})

'''
funcao auxiliar que retorna a lista de previsoes dee uma cidade formatada
'''
def previsoes(cidade, uf, pais):
    try:
        out = []
        for i in Previsao.query.filter_by(cidade=cidade,uf=uf,pais=pais).all():
            aux = {}
            for key,val in i.__dict__.items():
                if key == '_sa_instance_state' or key == 'id' or key == 'id' or key == 'cidade' or key == 'uf' or key == 'pais':
                    continue
                aux[str(key)] =  str(val) if key == 'date' else val
            out.append(aux)

        return {
            'cidade' : cidade,
            'uf' : uf,
            'pais' : pais,
            'previsoes' : out
        }
    except:
        raise

