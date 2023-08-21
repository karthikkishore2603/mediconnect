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

def get_doctor_by_id(admin_id: int) -> models.Hospital:
    return models.Hospital.query.filter_by(hospital_id=admin_id).first()

def get_all_doctors() -> models.Doctor:
    return models.Doctor.query.all()

def patient_add(data: dict) -> None:
    

    user = models.Patient(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()


def get_all_patient() -> models.Patient:
    return models.Patient.query.all()