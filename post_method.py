from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class item(BaseModel):
    title: str 
    body: str
    published : Optional[bool]



@app.get("/")
def home_path():
    return {"hello":"sir"}

@app.post("/blog")
def post_blog(request:item):
    return {"message":f"blog is created having title {request.title} having content as {request.body} and it was published on {request.published} "}


# note: when you need to send data from client to server, you need to send it in from of request Body
# a request body is data send by client to api 

# and to declare a request body ... we will need a pydantic model 
# and then pass that as typechecking in function 


# learn to debug also 