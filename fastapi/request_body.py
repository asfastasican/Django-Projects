from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#crreating the User schema using Basemodel for data validation
class User(BaseModel):
    name:str
    password:str
    address:str

app=FastAPI()

@app.post('/items')
def index(user:User):   #passing the requestbody data using USER
    print(user.address)
    return user

@app.post('/user/{user_id}')
def index(user_id:int,user:User):
    return user_id,user

@app.get("/")
def index(q:Optional[int]=None):
    return "This is testing of optional Q"