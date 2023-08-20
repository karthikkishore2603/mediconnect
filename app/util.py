from flask import request, url_for, Request
from datetime import datetime, timedelta
from typing import Union

from . import crud, constants

def is_valid_password(username, password, role):
    if crud.get_password(username, role) == password:
        return True
    else:
        return False