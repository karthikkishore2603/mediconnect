from flask import request, url_for, Request
from datetime import datetime, timedelta
from typing import Union

from . import crud, constants,schemas

def is_valid_password(username, password):
    if crud.get_password(username) == password:
        return True
    else:
        return False
    
def create_access_token(
    data: schemas.TokenData, expires_delta: Union[timedelta, None] = None
):
    to_encode = dict(data).copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=constants.ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, constants.SECRET_KEY, algorithm=constants.ALGORITHM
    )
    return encoded_jwt
