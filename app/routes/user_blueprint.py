from flask import Blueprint
from app.controllers.user_controllers import create, get_user, login

bp = Blueprint("bp_user",__name__, url_prefix="/users")
bp.post("")(create)
bp.post("/login")(login)
bp.get("")(get_user)