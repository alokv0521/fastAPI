from pydantic import BaseModel

class item(BaseModel):
    title: str
    body: str  # ✅ must match your Blog model

class show(BaseModel):
     #as ofnow, this will through error as we are not mentionning pydantic to use in orm mode
     body:str
     class config():
          orm_mode=True #here we are cinfiguring pydantic class in orm mode as it is giving orm response
          

class getAll(BaseModel):
     title:str
     body:str
     class config():
          orm_mode=True


class use(BaseModel):
     name:str
     email:str
     password:str

