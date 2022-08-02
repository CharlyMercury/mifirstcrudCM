## Python 
from typing import List
from cryptography.fernet import Fernet

## FastAPI
from fastapi import APIRouter, status
from fastapi import Body
from sqlalchemy import column

## Database
from config.db import conn

## Models
from models.user import users

## Schemas
from schemas.users import User, UserOut

## Inicializamos Fernet
key = Fernet.generate_key()
f = Fernet(key)

usersapp = APIRouter()

@usersapp.get(
    path = "/users",
    tags=["users"],
    response_model=List[UserOut],
    status_code = status.HTTP_200_OK,
    )
def users_list():
    return conn.execute(users.select()).fetchall()


@usersapp.post(
    path = "/users",
    tags = ["users"],
    response_model= UserOut,
    status_code=status.HTTP_201_CREATED,
    )
def create_user(new_user: User=Body(...)):
    new_user_db = new_user.dict()
    new_user_db['password'] = f.encrypt(new_user.password.encode('utf-8'))
    result = conn.execute(users.insert().values(new_user_db))
    return conn.execute(users.select().where(users.c.id==result.lastrowid)).first()



@usersapp.put(path = "/users/{user_id}")
def update():
    return {"hellow":"CharlyMercury"}


@usersapp.delete(path = "/users/{user_id}")
def delete():
    return {"hellow":"CharlyMercury"}

