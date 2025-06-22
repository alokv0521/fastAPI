from schemas import use
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from models import get_db, User
from hash import Hash


def put_user(request:use, db :Session=Depends(get_db)):
    new_user=User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return(new_user)


def get_user(id:int, db :Session=Depends(get_db)):
    new_user=db.query(User).filter(User.id==id).first()
    if new_user:
        return new_user
    else:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"the user with the id:{id} is not found")

