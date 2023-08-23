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
    hospital_username = Column(String(100), nullable=False, unique=True)
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
    patient_phoneno = Column(String(100), nullable=False,unique=True)
    patient_address = Column(String(100), nullable=False)
    patient_dob= Column(String(100), nullable=False)
    patient_password = Column(String(25))

class Appointment(db.Model):
    __tablename__ = "appointment"
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_date = Column(String(100), nullable=False)
    appointment_time = Column(String(100), nullable=False)
    appointment_patient_id = Column(Integer, ForeignKey('patient.patient_id'), nullable=False)
    appointment_doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'), nullable=False)
    appointment_hospital_id = Column(Integer, ForeignKey('hospital.hospital_id'), nullable=False) 
    appointment_reason = Column(String(100), nullable=False)
    appointment_specialization = Column(String(100), nullable=False)
    appointment_type = Column(String(100), nullable=False)




    
db.create_all()