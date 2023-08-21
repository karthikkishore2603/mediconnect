from flask import request, url_for, Request
from datetime import datetime, timedelta
from typing import Union
from jose import jwt, JWTError

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

def current_user_info(request: Request):
    token = request.cookies.get(constants.AUTH_TOKEN_COOKIE_NAME)
    if not token:
        return
    login = get_current_user_login(token)
    if not login:
        return
    return crud.get_doctor_by_id(login.id)
    #raise NotImplementedError

def get_current_user_login(token: str) -> Union[schemas.TokenData, None]:
    try:
        payload = jwt.decode(
            token, constants.SECRET_KEY, algorithms=[constants.ALGORITHM]
        )
        username: str = payload.get("username")
        id: str = payload.get("id")
        user_type: str = payload.get("user_type")
        if not username or not id or not user_type:
            return None
        token_data = schemas.TokenData(username=username, id=id, user_type=user_type)
    except JWTError:
        return None
    return token_data

def is_patient_valid_password(patient_phoneno, patient_password):
    if crud.get_patient_password(patient_phoneno) == patient_password:
        return True
    else:
        return False