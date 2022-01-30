from app.configs.database import db
from sqlalchemy import Column, Integer, String, REAL

class Electric(db.Model):
    __tablename__ = "electricity_providers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    logo = Column(String, nullable=False)
    state = Column(String, nullable=False)
    price_kwh = Column(REAL, nullable=False)
    mininum_limit_kwh = Column(REAL, nullable=False)
    number_of_clients = Column(Integer, nullable=False)
    average_rating = Column(REAL, nullable=False)