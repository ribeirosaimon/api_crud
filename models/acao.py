



class CarteiraModel:
    def __init__(self, acao_id, acao, preco_medio):
        self.acao_id = acao_id
        self.acao = acao
        self.preco_medio = preco_medio

    def json(self):
        return {
            'acao_id':self.acao_id,
            'acao':self.acao,
            'preco_medio':self.preco_medio
        }
