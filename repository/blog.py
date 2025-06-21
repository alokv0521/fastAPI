
from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException ,status
from models import get_db, Blog
from schemas import item

def retrieve(db :Session=Depends(get_db)):
    blogs=db.query(Blog).all()
    return blogs

def get_parti(id: int, db :Session=Depends(get_db)):
    blog= db.query(Blog).filter(Blog.id==id).first()
    if blog :
        return blog
    else : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there is no blog containing for the id: {id}"
        )
    
def make_blog(request:item , db :Session=Depends(get_db)):
    new_blog=Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return(new_blog)
 
def destroy(id, db :Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id).first()
    if not blog :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the blog with the id: {id} not exist ")
    else:
        db.query(Blog).filter(Blog.id==id).delete(synchronize_session=False)
    db.commit()
    raise HTTPException( status_code=status.HTTP_200_OK, detail= f"blog with the id:{id} got suscessfully deleted 🤗")

def update(id,request:item, db :Session=Depends(get_db)):
    db.query(Blog).filter(Blog.id==id).update({"title":request.title, "body":request.body}, synchronize_session=False )  
    db.commit()
    return {"suscessfully updated the record having id: {id}"}