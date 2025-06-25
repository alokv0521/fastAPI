from fastapi import APIRouter , Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import get_db, User
from schemas import login
from hash import Hash
from JWTTokens import create_access_token


auth=APIRouter(prefix="/login",
    tags=["authentication"]
)

@auth.post("/")
def login(request:login,  db:Session=Depends(get_db)):
    user=db.query(User).filter(User.name== request.username).first()
    if not user :
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"user not found")
    if not Hash.verify(request.password, user.password):
         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"incorrect pass")
    
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)optional
    access_token = create_access_token(data={"sub": user.name})
    return {"acess_token":access_token, "token_type":"bearer"}

