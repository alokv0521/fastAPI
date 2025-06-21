
from fastapi import Depends , status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import get_db, Blog
from schemas import item, show
from repository import blog

alok=APIRouter(
    tags=["Blogs"]
)

# get

@alok.get("/blog")
def get_All(db :Session=Depends(get_db)):
    
    return blog.retrieve(db)

# get with id 
@alok.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=show)
def retrieve(id:int, db :Session=Depends(get_db)):
    return blog.get_parti(id, db)
    
# post    
@alok.post("/blog", status_code=status.HTTP_201_CREATED) 
def get_blog(request:item , db :Session=Depends(get_db)):
    return blog.make_blog(request, db)
    


# delete
@alok.delete("/blog/{id}")
def astroid_destroyer(id, db :Session=Depends(get_db)):
    return blog.destroy(id, db)


# update
@alok.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id,request:item, db :Session=Depends(get_db)):
    return blog.update(id, request, db)
