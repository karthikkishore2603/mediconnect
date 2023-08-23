from . import *
from . import db, models, util
from sqlalchemy import distinct
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

def get_patient_by_id(patient_id: int) -> models.Patient:
    return models.Patient.query.filter_by(patient_id=patient_id).first()

def get_hospital_id_by_username(username: str):
    hospital = models.Hospital.query.filter_by(hospital_username=username).first()
    if hospital:
        return hospital.hospital_id
    return None


def get_doctor_by_id(doctor_id: int) -> models.Doctor:
    return models.Doctor.query.filter_by(doctor_id=doctor_id).first()


def get_all_doctors() -> models.Doctor:
    return models.Doctor.query.all()


def get_all_hospital() -> models.Hospital:
    return models.Hospital.query.all()


def get_all_city():
    return [
        i[0]
        for i in models.Hospital.query.with_entities(models.Hospital.hospital_city)
        .distinct()
        .all()
    ]


def get_hospital_by_city(city: str) -> models.Hospital:
    return models.Hospital.query.filter_by(hospital_city=city).all()

def get_doctors_by_hospital(hospital_id: list) -> models.Doctor:
    return models.Doctor.query.filter_by(doctor_hospital_id=hospital_id).distinct().all()

def get_hospital_specialization(hospital_id) -> models.Doctor:
    return  db.session.query(models.Doctor.specialization).filter_by(doctor_hospital_id=hospital_id).distinct().all()

def get_doctors_by_specialization(sp) -> models.Doctor:
    return models.Doctor.query.filter_by(specialization=sp).distinct().all()

def patient_add(data: dict) -> None:
    user = models.Patient(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()


def get_all_patient() -> models.Patient:
    return models.Patient.query.all()

def is_patient_exists(patient_phno):
    patient = models.Patient.query.filter_by(patient_phoneno=patient_phno).first()
    if patient:
        return True
    return False

def get_patient_id(patient_phno):
    patient = models.Patient.query.filter_by(patient_phoneno=patient_phno).first()
    if patient:
        return patient.patient_id
    return None

def appointment_add(data):
    user = models.Appointment(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()

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
