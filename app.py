from flask import Flask
from flask_restful import Api
from resources.carteira import Carteira, Acao

app = Flask(__name__)
api = Api(app)




api.add_resource(Carteira, '/carteira')
api.add_resource(Acao, '/carteira/<int:acao_id>')

if __name__ == '__main__':
    app.run(debug=True)
