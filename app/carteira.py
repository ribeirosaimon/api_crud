from flask import Blueprint, current_app, request
from .model import Carteira
from .serealizer import CarteiraSchema

bp_carteira = Blueprint('carteira', __name__)

@bp_carteira.route('/mostrar', methods=['GET'])
def mostrar():
    cs = CarteiraSchema(many=True)
    result=Carteira.query.all()
    return cs.jsonify(result), 200

@bp_carteira.route('/deletar', methods=['GET'])
def deletar(identificador):
    Carteiar.query.filter(Carteira.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!')

@bp_carteira.route('/modificar', methods=['POST'])
def modificar(identificador):
    cs = CarteiraSchema()
    query = Carteira.query.filter(Carteira.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return cs.jsonify(query.firts())

@bp_carteira.route('/cadastrar', methods=['POST'])
def cadastrar():
    cs = CarteiraSchema()
    carteira, error = cs.load(request.json)
    current_app.db.session.add(carteira)
    current_app.db.session.commit()
    return cs.jsonify(carteira), 201
