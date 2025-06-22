from fastapi import APIRouter , Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import get_db, User
from schemas import login
from hash import Hash

auth=APIRouter(prefix="/login",
    tags=["authentication"]
)

@auth.post("/login")
def login(request:login,  db:Session=Depends(get_db)):
    user=db.query(User).filter(User.name== request.username).first()
    if not user :
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"user not found")
    if not Hash.verify(request.password, user.password):
         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"incorrect pass")
    return {"acess granted suscessfully"}
