from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from schemas import use, user_incrypted
from sqlalchemy.orm import Session
from models import User, get_db
from repository import user_fun

nilesh=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@nilesh.post("/", response_model=user_incrypted)
def user(request:use, db :Session=Depends(get_db)):
    return user_fun.put_user(id, db)
    



@nilesh.get("/{id}", response_model=user_incrypted, status_code=status.HTTP_200_OK)
def retrieve_user(id:int, db :Session=Depends(get_db)):
    return user_fun.get_user(id, db)
    