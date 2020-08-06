from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Carteira(Resource):
    def get(self):
        return {'acao':'movi3','preco_medio':'15.8'}


api.add_resource(Carteira, '/carteira')

if __name__ == '__main__':
    app.run(debug=True)
