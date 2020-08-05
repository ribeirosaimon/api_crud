from flask_marshmallow import Marshmallow
from .model import Carteira

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class CarteiraSchema(ma.Schema):
    class Meta:
        model = Carteira
