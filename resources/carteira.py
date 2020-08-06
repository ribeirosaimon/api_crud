from flask_restful import Resource, reqparse
from models.acao import CarteiraModel


class Carteira(Resource):
    def get(self):
        return {'carteira':carteira}

class Acao(Resource):
    args = reqparse.RequestParser()
    args.add_argument('acao')
    args.add_argument('preco_medio')



    def get(self, acao_id):
        acao = CarteiraModel.find_acao(acao_id)
        if acao:
            return acao.json()
        return {'message':'Stock not found.'}, 404


    def post(self, acao_id):
        if CarteiraModel.find_acao(acao_id):
            return {'message': f"Stock id '{acao_id}' already exists."}, 400
        dados = Acao.args.parse_args()
        acao = CarteiraModel(acao_id, **dados)
        acao.save_acao()
        return acao.json(), 200

    def put(self, acao_id):
        dados = Acao.args.parse_args()
        acao_objeto = CarteiraModel(acao_id, **dados)
        nova_acao = acao_objeto.json()
        acao = Acao.find_acao(acao_id)
        if acao:
            acao.update(nova_acao)
            return nova_acao, 200
        acao.append(nova_acao)
        return nova_acao, 201

    def delete(self, acao_id):
        global carteira
        carteira = [acao for acao in carteira if acao['acao_id'] != acao_id]
        return {'message':'Stock deleted.'}
