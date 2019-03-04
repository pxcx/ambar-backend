from config import app
from views import coleta, temperatura_maxima, precipitacao, probabilidade


# rota: / - exibe a documentacao da api
@app.route('/', methods=['GET'])
def index():
	return jsonify({ 'status' : 'API running...'})

# rota: /coleta - faz a coleta dos dados da cidade informada como parametro
# - cidade (string)
# - uf (string)
coleta.configure(app)

# rota: /temperatura-maxima - retorna a cidade com a temperatura maxima
# - inicio (YYYY-MM-DD)
# - fim (YYYY-MM-DD)
temperatura_maxima.configure(app)

# rota: /precipitacao - retorna uma lista de média de precipitacao por cidade
# - inicio (YYYY-MM-DD)
# - fim (YYYY-MM-DD)
precipitacao.configure(app)

# /probabilidade - retorna a probabilidade total de chuva
# - inicio (YYYY-MM-DD)
# - fim (YYYY-MM-DD)
probabilidade.configure(app)

if __name__ == "__main__":
    app.run(debug=True)