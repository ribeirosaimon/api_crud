from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
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

carteira = {}

def se_acao_nao_existir(acao_id):
    if acao_id not in carteira:
        abort(404, message='Não consigo achar essa ação')

def se_ja_existir_acao(acao_id):
    if acao_id in carteira:
        abort(404, message='Essa ação já existe')


class Carteira(Resource):
    def get(self, acao_id):
        se_acao_nao_existir(acao_id)
        return carteira[acao_id]

    def put(self, acao_id):
        se_ja_existir_acao(acao_id)
        args = carteira_put_args.parse_args()
        carteira[acao_id] = args
        return carteira[acao_id], 201

    def delete(self, acao_id):
        se_acao_nao_existir(acao_id)
        del carteira[acao_id]
        return '', 204

api.add_resource(Carteira, '/carteira/<int:acao_id>')

if __name__ == '__main__':
    app.run(debug=True)
