from config import db
'''
model da tabela previsoes
'''
class Previsao(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	cidade = db.Column(db.String(255), nullable=False)
	uf = db.Column(db.String(2), nullable=False)
	pais = db.Column(db.String(2), nullable=False)
	date = db.Column(db.Date, nullable=False)
	chuva_probabilidade = db.Column(db.Integer, nullable=False)
	chuva_precipitacao = db.Column(db.Integer, nullable=False)
	temperatura_min = db.Column(db.Integer, nullable=False)
	temperatura_max = db.Column(db.Integer, nullable=False)