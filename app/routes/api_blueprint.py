from flask import Blueprint
from app.routes.eletric_blueprint import bp as bp_electric
from app.routes.user_blueprint import bp as bp_user

bp = Blueprint("bp_api",__name__, url_prefix="/api")
bp.register_blueprint(bp_electric)
bp.register_blueprint(bp_user)