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

home_route_info={"messge": "welcome to sacred place of temples and we are"}
# decorator
@app.get("/")
def read_root():
    return home_route_info

# note: function name doesn't matter ..only the thing that matter is the decorator 

# here routs are called path in some frameworks these are called api endpoints

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
# uvicorn name_of_file(here_main) : name of fast api instance( here app) -- reload 
# run it using uvicorn 


# theroy

# here get , put , post  , delete .. these are called operation on path 
# the function on which we are deciding is called path operation function
# def read_root():
#     return home_route_info 
# is the operation that we are going to perform on "/" path 

# @app decorator is callled path operation decorator 
