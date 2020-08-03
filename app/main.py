from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

carteira_put_args = reqparse.RequestParser()
carteira_put_args.add_argument('acao', type=str, help='Papel da Empresa', required=True)
carteira_put_args.add_argument('pm', type=int, help='Preço Médio', required=True)

carteira = {}


class Carteira(Resource):
    def get(self, acao_id):
        return carteira[acao_id]

    def put(self, acao_id):
        args = carteira_put_args.parse_args()
        carteira[acao_id] = args
        return carteira[acao_id], 201

api.add_resource(Carteira, '/carteira/<int:acao_id>')

if __name__ == '__main__':
    app.run(debug=True)
