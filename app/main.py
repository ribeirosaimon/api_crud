from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class CarteiraModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acao = db.Column(db.String(15), nullable=False)
    pm = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return  f'Carteira(Ação: {acao}, preco_medio: {pm})'

db.create_all()



carteira_put_args = reqparse.RequestParser()
carteira_put_args.add_argument('acao', type=str, help='Papel da Empresa', required=True)
carteira_put_args.add_argument('pm', type=float, help='Preço Médio', required=True)


resource_fields = {
	'id': fields.Integer,
	'acao': fields.String,
	'pm': fields.Float
}



class Carteira(Resource):
	@marshal_with(resource_fields)
	def get(self, acao_id):
		result = CarteiraModel.query.filter_by(id=acao_id).first()
		if not result:
			abort(404, message="Could not find stock with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, acao_id):
		args = carteira_put_args.parse_args()
		result = CarteiraModel.query.filter_by(id=acao_id).first()
		if result:
			abort(409, message="Ação id taken...")

		acao = CarteiraModel(id=acao_id, acao=args['acao'], pm=args['pm'])
		db.session.add(acao)
		db.session.commit()
		return acao, 201

api.add_resource(Carteira, '/carteira/<int:acao_id>')

if __name__ == '__main__':
    app.run(debug=True)
