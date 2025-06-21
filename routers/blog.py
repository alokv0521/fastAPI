
from fastapi import Depends , status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import get_db, Blog
from schemas import item, show

alok=APIRouter(
    tags=["Blogs"]
)

# get

@alok.get("/blog")
def get_All(db :Session=Depends(get_db)):
    blogs=db.query(Blog).all()
    return blogs

# get with id 
@alok.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=show)
def retrieve(id:int, db :Session=Depends(get_db)):
    blog= db.query(Blog).filter(Blog.id==id).first()
    if blog :
        return blog
    else : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there is no blog containing for the id: {id}"
        )
    
# post    
@alok.post("/blog", status_code=status.HTTP_201_CREATED) 
def get_blog(request:item , db :Session=Depends(get_db)):
    new_blog=Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return(new_blog)


# delete
@alok.delete("/blog/{id}")
def astroid_destroyer(id, db :Session=Depends(get_db)):

    blog = db.query(Blog).filter(Blog.id==id).first()
    if not blog :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the blog with the id: {id} not exist ")
    else:
        db.query(Blog).filter(Blog.id==id).delete(synchronize_session=False)
    db.commit()
    raise HTTPException( status_code=status.HTTP_200_OK, detail= f"blog with the id:{id} got suscessfully deleted 🤗")


# update
@alok.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id,request:item, db :Session=Depends(get_db)):
    db.query(Blog).filter(Blog.id==id).update({"title":request.title, "body":request.body}, synchronize_session=False )  
    db.commit()
    return {"suscessfully updated the record having id: {id}"}
