from flask_restful import Resource, reqparse
from models.acao import CarteiraModel

carteira = [
    {
    'acao_id':0,
    'acao':'movi3',
    'preco_medio':15.8
    },
    {
    'acao_id':1,
    'acao':'shul4',
    'preco_medio':11.2
    },
    {
    'acao_id':2,
    'acao':'tcsa3',
    'preco_medio':10.44
    }
]



class Carteira(Resource):
    def get(self):
        return {'carteira':carteira}

class Acao(Resource):
    args = reqparse.RequestParser()
    args.add_argument('acao')
    args.add_argument('preco_medio')

    def find_acao(acao_id):
        for acao in carteira:
            if acao['acao_id'] == acao_id:
                return acao
        return None

    def get(self, acao_id):
        acao = Acao.find_acao(acao_id)
        if acao:
            return acao
        return {'message':'Stock not found.'}, 404


    def post(self, acao_id):
        dados = Acao.args.parse_args()
        acao_objeto = CarteiraModel(acao_id, **dados)
        nova_acao = acao_objeto.json()
        carteira.append(nova_acao)
        return nova_acao, 200

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
