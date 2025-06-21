from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from schemas import item ,show , getAll, use, user_incrypted
from sqlalchemy.orm import Session
from models import Blog, User, get_db
from database import engine, Base
from typing import List
from hash import hash

nilesh=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@nilesh.post("/", response_model=user_incrypted)
def user(request:use, db :Session=Depends(get_db)):
    # hash_pass=pwd_context.hash(request.password)
    new_user=User(name=request.name, email=request.email, password=hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return(new_user)

@nilesh.get("/{id}", response_model=user_incrypted, status_code=status.HTTP_200_OK)
def retrieve_user(id:int, db :Session=Depends(get_db)):
    new_user=db.query(User).filter(User.id==id).first()
    if new_user:
        return new_user
    else:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"the user with the id:{id} is not found")
    