from flask import (
    make_response,
    redirect,
    render_template,
    request,
    url_for,
    request,
)

from .. import app, crud, util, constants, schemas
from datetime import timedelta, datetime
import pytz


@app.get("/")
def login():
    # Check if it's already authenticate
    """if util.is_user_authenticated(request) or util.is_user_authenticated(request, type="admin"):
        token = request.cookies.get(constants.AUTH_TOKEN_COOKIE_NAME)
        user = util.get_current_user_login(token)
        if user.user_type == "admin":
            return redirect(url_for("admin_dashboard"))
        elif user.user_type == "technician":
            return redirect(url_for("tech_dashboard"))
        else:
            return render_template("check.html", error_message="Invalid user type")"""
    return render_template("login.html")


@app.post("/")
def login_verify():
    username = request.form.get("username")
    password = request.form.get("password")
    if not util.is_valid_password(username, password):
        return render_template("check.html")
    access_token_expires = timedelta(days=constants.ACCESS_TOKEN_EXPIRE_DAYS)
    response = make_response(redirect(url_for("doctor_dashboard")))
    return response
    """
    if role == "admin":
        admin_login = crud.get_admin(username=username)

        response = make_response(redirect(url_for("admin_dashboard")))

        jwt_token = util.create_access_token(
            schemas.TokenData(
                username=username,
                id=admin_login.admin_id,
                user_type="admin",
            ),
            access_token_expires,
        )

        response.set_cookie(
            constants.AUTH_TOKEN_COOKIE_NAME,
            jwt_token,
            expires=(datetime.now(pytz.timezone('Asia/Kolkata')) + access_token_expires),
        )
        return response

    else:
        return render_template("check.html", error_message="Invalid user type")
"""

@app.get("/logout")
def logout():
    # remove the token from the cookie
    response = redirect(url_for("login"))
    response.set_cookie(constants.AUTH_TOKEN_COOKIE_NAME, "")
    return response


@app.get("/patient/login")
def patient_login():
    return render_template("patient_login.html")

@app.post("/patient/login")
def patient_login_post():
    patient_phoneno = request.form.get("patient_phoneno")
    patient_password = request.form.get("patient_password")
    if not util.is_patient_valid_password(patient_phoneno, patient_password):
        return render_template("check.html")
    access_token_expires = timedelta(days=constants.ACCESS_TOKEN_EXPIRE_DAYS)
    response = make_response(redirect(url_for("patient_dashboard")))
    return response