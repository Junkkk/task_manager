from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    password: str


class Task(BaseModel):
    name: str
    description: str
    date: date
    status: str
    end_date: date = None
