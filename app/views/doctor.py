from flask import render_template, request, redirect, url_for, make_response,json,Response, jsonify
import pymysql
import time 
from datetime import datetime
from .. import app, crud, util, models
#from fpdf import FPDF
#import pytz


@app.get("/doctor_dashboard")
def doctor_dashboard():
    return render_template("doctor_dashboard.html")