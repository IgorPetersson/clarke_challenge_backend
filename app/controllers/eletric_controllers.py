from app.models.eletric_models import Electric
from http import HTTPStatus
from flask_jwt_extended import jwt_required

@jwt_required()
def get_provider_for_kwh(kwh):
    providers_electric = Electric.query.filter(Electric.mininum_limit_kwh < kwh).all()
    providers = [{
        "id": provider.id,
        "name": provider.name,
        "logo": provider.logo,
        "state": provider.state,
        "minimum_limit_khw": provider.mininum_limit_kwh,
        "average_rating": provider.average_rating,
        "number_of_clients": provider.number_of_clients,
        "price_kwh": provider.price_kwh
    } for provider in providers_electric]

    return {"data": providers}, HTTPStatus.OK
   