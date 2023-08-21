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
    hospital = util.current_user_info(request)
    print(hospital)
    return render_template("doctor_appointment.html",hospital = hospital )

@app.get("/doctor/details")
def doctor_details():
    
    hospital = util.current_user_info(request)
    
    print(hospital)
    return render_template("doctor_details.html",a=hospital.hospital_id,doctors = crud.get_all_doctors()) 

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
    print( crud.get_doctor_by_id(doctor_id))
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