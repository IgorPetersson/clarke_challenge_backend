from app.exceptions.users_exceptions import KeysMissing, ToManyKeys, KeysTypeError, EmailAlreadyExists, UserNotAuthorized, UserNotFound
from app.models.user_models import User
from flask import request, current_app
from http import HTTPStatus
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

def validate_create(data):
    important_keys = ["name","email", "password"]

    keys_missing = []
    for key in important_keys:
        if key not in data.keys():
            keys_missing.append(key)

    if len(keys_missing) > 0:
        raise KeysMissing("Keys missing: " + ", ".join(keys_missing))

    many_keys = []
    for key in data.keys():
        if key not in important_keys:
            many_keys.append(key)
    
    if len(many_keys) > 0:
        raise ToManyKeys("Keys not allowed: " + ", ".join(many_keys))

    for valueType in data.values():
        if type(valueType) != str:
            raise KeysTypeError("All keys must be string")

    users = User.query.all()
    users_email = [user.email for user in users]

    if data["email"] in users_email:
        raise EmailAlreadyExists("This email is already registered in the system")

def validate_login(user, password):
    if user == None:
        raise UserNotFound("User not registered in the system")
    login_is_true = check_password_hash(user.password, password)
    if login_is_true == False:
        raise UserNotAuthorized("Password and email combination is incorrect")

def create():
    try:
        data = request.get_json()
        validate_create(data)
        password_hash = data.pop("password")
        data['password'] =generate_password_hash(password_hash)
        user = User(**data)
        current_app.db.session.add(user)
        current_app.db.session.commit()

        user_serializer = {
            "id": user.id,    
            "name": user.name,
            "email": user.email
            } 

        return {"data": user_serializer}, HTTPStatus.OK
    except KeysMissing as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST
    except ToManyKeys as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST
    except KeysTypeError as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST
    except EmailAlreadyExists as e:
        return {"msg": str(e)}, HTTPStatus.CONFLICT

def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data["email"]).first()
        validate_login(user, data["password"])

        user_serializer = {
            "name": user.name,
            "email": user.email,
            "id": user.id
        } 

        access_token = create_access_token(identity=user_serializer)
        return {"access_token": access_token}, HTTPStatus.OK
    except UserNotAuthorized as e:
        return {"msg": str(e)}, HTTPStatus.UNAUTHORIZED
    except UserNotFound as e:
        return {"msg": str(e)}, HTTPStatus.NOT_FOUND