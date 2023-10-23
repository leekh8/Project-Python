from flask_sqlalchemy import SQLAlchemy
from ..config import config

db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
    # Optionally, to suppress warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
