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
    return render_template("patient_dashboard.html")

@app.get("/patient/appoinment")
def patient_appoinment():

    return render_template("patient_appointment.html",hs = crud.get_all_hospital())