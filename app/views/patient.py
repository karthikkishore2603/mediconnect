from flask import render_template, request, redirect, url_for, make_response,json,Response, jsonify
import pymysql
import time 
from datetime import datetime
from .. import app, crud, util, models
#from fpdf import FPDF
#import pytz

"""
@app.get("/parient/dashboard")
def doctor_dashboard():
    return render_template("doctor_dashboard.html")

@app.get("/doctor/apointment")
def doctor_apointment():
    return render_template("doctor_appointment.html")"""