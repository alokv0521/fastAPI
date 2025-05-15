from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# fast api for framework 
# pydantic for validation 
# we can define it in base model 

app=FastAPI();

class Temp(BaseModel):
    id: int
    name: str
    place:str

temple_db : List[Temp]=[]


# decorator
@app.get("/")
def read_root():
    return {"messge": "welcome to sacred place of temples"}

@app.get("/temple") # decorator
def ret_temp():     #function
    return temple_db

@app.post("/temple")
def add_temp(temple : Temp):
    temple_db.append(temple)
    return (temple)

# @app.put("/temple/{temple_id}")
# def update_temple(temp_id : int , updated_temp_info : Temp):
#     for index, temp in enumerate(temple_db):
#         if temp.id = temp_id:


# now how to run this 

# run it using uvicorn 