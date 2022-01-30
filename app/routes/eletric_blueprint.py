from flask import Blueprint
from app.controllers.eletric_controllers import get_provider_for_kwh

bp = Blueprint("bp_electric", __name__, url_prefix="/electric")
bp.get("/limit/<int:kwh>")(get_provider_for_kwh)