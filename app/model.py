from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Carteira(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acao = db.Column(db.String(15))
    preco_medio = db.Column(db.Float())
