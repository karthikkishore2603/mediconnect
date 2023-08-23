from flask import render_template, request, redirect, url_for, make_response,json,Response, jsonify
import pymysql
import time 
from datetime import datetime
from .. import app, crud, util, models
#from fpdf import FPDF
#import pytz


@app.get("/doctor/dashboard")
def doctor_dashboard():
    return render_template("doctor_dashboard.html")

@app.get("/doctor/apointment")
def doctor_apointment():
    hospital_req = util.current_user_info(request)
    return render_template("doctor_appointment.html",
                           hospital_id=hospital_req.hospital_id,
                           doctors = crud.get_doctors_by_hospital(hospital_req.hospital_id),
                           hospital = crud.get_all_hospital())

@app.post("/doctor/apointment")
def doctor_apointment_post():
    hospital_req = util.current_user_info(request)
    data = dict(request.form)
    patient_phno = data.get("patient_phoneno")
    if crud.is_patient_exists(patient_phno):
        patient_id = crud.get_patient_id(patient_phno)
        data["appointment_patient_id"] = patient_id
    else:
        return render_template("doctor_appointment.html",
                           hospital_id=hospital_req.hospital_id,
                           doctors = crud.get_doctors_by_hospital(hospital_req.hospital_id),
                           hospital = crud.get_all_hospital(),
                           error="Patient not found")
    dict.pop(data,'patient_phoneno')
    if data.get("ftype"):
        redirect(url_for("doctor_apointment"))
    try:
        crud.appointment_add(data)
        print(data)
    except Exception as e:
        print(e)
        return redirect(url_for("doctor_apointment"))
    return redirect(url_for("doctor_apointment"))

@app.get("/doctor/details")
def doctor_details():
    hospital = util.current_user_info(request)
    
    return render_template("doctor_details.html",
                           hospital_id=hospital.hospital_id,

                           doctors = crud.get_doctors_by_hospital(hospital.hospital_id)) 

@app.post("/doctor/details")
def doctor_details_post():
    admin = util.current_user_info(request)
    print(admin.hospital_id)
    data = dict(request.form)
    if data.get("ftype"):
        redirect(url_for("doctor_details"))
    try:
        crud.doctor_details(data)
        print(data)
    except Exception as e:
        print(e)
        return redirect(url_for("doctor_details"))
    return redirect(url_for("doctor_details"))

@app.get("/doctor/details/<doctor_id>")
def get_doctor_by_id(doctor_id):
    print(crud.get_doctor_by_id(doctor_id))
    return render_template("doctor_per_detail.html", doctor = crud.get_doctor_by_id(doctor_id))

@app.get("/doctor/patient")
def doctor_patient():
    return render_template("doctor_patient.html", patients = crud.get_all_patient())

@app.post("/doctor/patient")
def doctor_patient_post():
    data= dict(request.form)
    if data.get("patient_password") == None:
        data["patient_password"] = data["patient_phoneno"]

    try:
        crud.patient_add(data)
    except Exception as e:
        print(e)
    return redirect(url_for("doctor_patient"))