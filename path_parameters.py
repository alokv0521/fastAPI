#here we will learn about dynamic rounting and path parameters 



from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



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



@app.get("/temple/{name}") # decorator
def ret_temp(name: int):     #function
    return {"message":name}

@app.post("/temple")
def add_temp(temple : Temp):
    temple_db.append(temple)
    return (temple)


# notes:
# you can give parameter in path and then pass them to the function and we can use it in giving message obviously by using {}
# can even define the type of argument we are asking for

# one more point to note:
# while creating a dynamic route/path you will need to carefully hadle the case of overlapping and conflict 
# for eg:
# @app.get("/temple/{name}")  "/temple/100"
# def tempnmae(name:int):
#     return{ "hello"+{name}}

# might get conflict with "/temple/shiva"
# so it should be need to be put before dynamic route .. bascially need to be handled with care 


# similarly we have querry parameters .. querry parameter is given after "?" sign ... read it a bit about in docs .. it will be easy