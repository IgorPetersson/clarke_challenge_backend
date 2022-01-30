from sre_parse import FLAGS
from flask import Flask
from app.configs import env_configs, jwt_auth, database, migrations, cors
from app import routes

def create_app():
    app = Flask(__name__)
    cors.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    env_configs.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)
    return app