from fastapi import FastAPI,Depends
from pydantic import BaseModel
from pymongo import MongoClient
app = FastAPI()

uri = 'mongodb://localhost/mydb'
client = MongoClient(uri)
database = client.get_database()

user_collection = database['user']


class User(BaseModel):
    username: str
    password: str

async def get_current_database():
    db = database
    yield db 

