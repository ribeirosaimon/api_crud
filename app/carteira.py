from flask import Blueprint

bp_carteira = Blueprint('carteira', __name__)

@bp_carteira.route('/mostrar', methods=['GET'])
def mostrar():
    ...
