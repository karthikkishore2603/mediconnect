from . import *
from . import db, models, util
from datetime import datetime

def get_password(username: str) -> str:
    password = models.Hospital.query.filter_by(hospital_username=username).first()

    if password:
        return password.hospital_password
    else:
        return None
