import email
from app.configs.database import db
from sqlalchemy import Column, Integer, String

class User(db.model):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True)
    name = Column(String, nullable=False)
    email =Column(String, nullable=False, unique=True)
    password = Column(String, name=False)
