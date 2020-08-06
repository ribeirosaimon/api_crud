from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////carteira.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    config_db(app)
    config_ma(app)


    Migrate(app, app.db)
    from .carteira import bp_carteira
    app.register_blueprint(bp_carteira)
    return app
