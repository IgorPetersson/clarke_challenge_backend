from flask import Blueprint
from app.controllers.user_controllers import create

bp = Blueprint("bp_user",__name__, url_prefix="/users")
bp.post("")(create)