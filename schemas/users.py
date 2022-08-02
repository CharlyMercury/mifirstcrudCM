## Python
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic.types import constr
from pydantic import Field

## MODELS
class User_Base(BaseModel):
    id: Optional[int]
    username: str = Field(
        ...,
        min_length = 1, 
        max_length = 50
    )
    email: EmailStr
    fullname: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    roll: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    address: str = Field(
        ...,
        min_length = 1,
        max_length = 100
    )
    city: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    country: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    postal_code: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    cel_number: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )


class User(User_Base):
    password: str = Field(
        ...,
        min_length = 1,
        max_length = 50,
    )
    class Config:
        schema_extra = {
            "example" : {
                "username" : "CarlitosAntonio",
                "email" : "carlos.mercury92@gmail.com",
                "fullname" : "Carlos Antonio Tovar Garcia",
                "roll" : "admin",
                "address" : "Leonardo Da Vinci #552 Col. Tecnológico",
                "city" : "Victoria",
                "country" : "México",
                "postal_code" : "87070",
                "cel_number" : "5545333530",
                "password" : "sdfaw4ra4tafwef",
            }
        }


class UserOut(BaseModel):
    id: Optional[int]
    username: str
    email: str
    fullname: str 
    roll: str
    address: str 
    city: str 
    country: str 
    postal_code: str 
    cel_number: str 