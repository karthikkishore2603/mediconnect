from flask import render_template, request, redirect, url_for, make_response,json,Response, jsonify
import pymysql
import time 
from datetime import datetime
from .. import app, crud, util, models
#from fpdf import FPDF
#import pytz


@app.get("/patient/register")
def patient_register():
    return render_template("patient_register.html")

@app.post("/patient/register")
def patient_register_post():
    data = dict(request.form)
    print(data)
    if data.get("patient_password") != data.get("patient_confirm_password"):
        return render_template("patient_register.html",error_message="Password and Confirm Password are not same")
    dict.pop(data,'patient_confirm_password')

    if data.get("patient_phoneno") == crud.get_patient_phoneno(data.get("patient_phoneno")):
        return render_template("patient_register.html",error_message="Phone Number Already Exists")

    try:
        crud.patient_add(data)
    except Exception as e:
        print(e)
        return render_template("patient_register.html",error_message="Phone Number Already Exists")
    return redirect(url_for("patient_login"))

@app.get("/patient/dashboard")
def patient_dashboard():
    patient = util.current_user_info(request)
    print(patient.patient_id)
    return render_template("patient_dashboard.html")

@app.get("/patient/appoinment")
def patient_appoinment():
    return render_template("patient_appointment.html",
                           cities=crud.get_all_city())

@app.post("/patient/appoinment")
def patient_appoinment_post():    
    patient = util.current_user_info(request)
    print(patient.patient_id)
          
    data = dict(request.form)
    print(data)
    data["appointment_patient_id"] = patient.patient_id
    dict.pop(data,'location')
    try:
        crud.appointment_add(data)
    except Exception as e:
        print(e)
        return render_template("patient_appointment.html",error_message="Something went wrong")
    #crud.appointment_add(data)
    return redirect(url_for("patient_dashboard"))

@app.get("/patient/appoinment/get-hospitals")
def patient_appoinment_get_hospitals():
    city = request.args.get("city")
    hospitals = crud.get_hospital_by_city(city)
    doctors = crud.get_doctors_by_hospital(hospitals[0].hospital_id)
    
    #hospital = crud.get_hospital_by_id(hospitals[0].hospital_id)
    return render_template("hospital_options.html",
                            hospitals=hospitals)

@app.get("/patient/appoinment/get-sp")
def patient_appoinment_get_specialization():
    hospital_id = request.args.get("hospital")
    sp = crud.get_hospital_specialization(hospital_id)
    
    doctors = crud.get_doctors_by_hospital(hospital_id)
    return render_template("hospital_options_sp.html",
                                sp = sp)

@app.get("/patient/appoinment/get-doctors")
def patient_appoinment_get_doctors():
    spe = request.args.get("speciality")
    print(spe)
    doctors = crud.get_doctors_by_specialization(spe)
    print(doctors)
    return render_template("hospital_options_doctors.html",doctors=doctors)

