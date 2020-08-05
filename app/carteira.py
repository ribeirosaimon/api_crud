from flask import Blueprint

bp_carteira = Blueprint('carteira', __name__)

@bp_carteira.route('/mostrar', methods=['GET'])
def mostrar():
    ...

@bp_carteira.route('/deletar', methods=['GET'])
def deletar():
    ...

@bp_carteira.route('/modificar', methods=['GET'])
def modificar():
    ...

@bp_carteira.route('/inserir', methods=['GET'])
def inserir():
    ...
