from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    from app.models.user_models import User
    from app.models.eletric_models import Electric
    db.init_app(app)
    app.db = db