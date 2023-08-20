from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .. import db


class Test(db.Model):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)

class Hospital(db.Model):
    __tablename__ = "hospital"
    hospital_id = Column(Integer, primary_key=True)
    hospital_name = Column(String(100), nullable=False)
    hospital_contact = Column(String(100), nullable=False)
    hospital_email = Column(String(100), nullable=False)
    hospital_address = Column(String(100), nullable=False)
    hospital_city = Column(String(100), nullable=False)
    hospital_state = Column(String(100), nullable=False)
    hospital_pincode = Column(String(100), nullable=False)
    hospital_country = Column(String(100), nullable=False)
    hospital_username = Column(String(100), nullable=False)
    hospital_password = Column(String(100), nullable=False)
    

db.create_all()