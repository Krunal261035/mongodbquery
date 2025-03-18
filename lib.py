from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

uri = "mongodb://localhost/library"
client = MongoClient(uri)
database = client.get_database()

users_collection = database['Books']

class Books(BaseModel):
    title: str
    author : str
    price: int

async def get_current_database():
    db = database
    yield db

@app.post("/insert_book")
async def insert(book_data:Books):
    books_id = insert_data(book_data)
    return {"message":"added successfully","books": str(books_id)}


def insert_data(book_data):
    book_dict = book_data.dict()
    result = users_collection.insert_one(book_dict)
    return result.inserted_id