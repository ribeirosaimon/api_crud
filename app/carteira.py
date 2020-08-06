from flask import Blueprint
from .model import Carteira
from .serealizer import CarteiraSchema

bp_carteira = Blueprint('carteira', __name__)

@bp_carteira.route('/mostrar', methods=['GET'])
def mostrar():
    cs = CarteiraSchema(many=True)
    result=Carteira.query.all()
    return cs.jsonify(result), 200

@bp_carteira.route('/deletar', methods=['GET'])
def deletar():
    ...

@bp_carteira.route('/modificar', methods=['GET'])
def modificar():
    ...

@bp_carteira.route('/inserir', methods=['GET'])
def inserir():
    ...
