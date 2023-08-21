from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .. import db


class Test(db.Model):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)

class Hospital(db.Model):
    __tablename__ = "hospital"
    hospital_id = Column(Integer, primary_key=True, autoincrement=True)
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

class Doctor(db.Model):
    __tablename__ = "doctor"
    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_name = Column(String(100), nullable=False)
    doctor_email = Column(String(100), nullable=False)
    doctor_address = Column(String(100), nullable=False)
    doctor_phoneno = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    doctor_dob= Column(String(100), nullable=False)
    doctor_hospital_id = Column(Integer, ForeignKey('hospital.hospital_id'), nullable=False)

class Patient(db.Model):
    __tablename__ = "patient"
    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_name = Column(String(100), nullable=False)
    patient_phoneno = Column(String(100), nullable=False)
    patient_address = Column(String(100), nullable=False)
    patient_dob= Column(String(100), nullable=False)
    patient_password = Column(String(25))




    
db.create_all()