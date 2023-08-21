from . import *
from . import db, models, util
from datetime import datetime

def get_password(username: str) -> str:
    password = models.Hospital.query.filter_by(hospital_username=username).first()

    if password:
        return password.hospital_password
    else:
        return None

def doctor_details(data: dict) -> None:
    

    user = models.Doctor(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()

def get_hospital_by_id(doctor_id: int) -> models.Hospital:
    return models.Hospital.query.filter_by(hospital_id=doctor_id).first()


def get_doctor_by_id(doctor_id: int) -> models.Doctor:
    return models.Doctor.query.filter_by(doctor_id=doctor_id).first()

def get_all_doctors() -> models.Doctor:
    return models.Doctor.query.all()

def get_all_hospital() -> models.Hospital:
    return models.Hospital.query.all()

def patient_add(data: dict) -> None:
    

    user = models.Patient(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()


def get_all_patient() -> models.Patient:
    return models.Patient.query.all()


#####################################################################################################################################3
#####################################################################################################################################
#####################################################################################################################################   
#####################################################################################################################################3


def get_patient_password(patient_phoneno: str) -> str:
    password = models.Patient.query.filter_by(patient_phoneno=patient_phoneno).first()

    if password:
        return password.patient_password
    else:
        return None
    
def get_patient_phoneno(patient_phoneno: str) -> str:
    phoneno = models.Patient.query.filter_by(patient_phoneno=patient_phoneno).first()

    if phoneno:
        return phoneno.patient_phoneno
    else:
        return None
        