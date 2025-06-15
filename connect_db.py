from fastapi import FastAPI, Depends, status
from schemas import item
from sqlalchemy.orm import Session
from models import Blog
from database import engine, Base, sessionlocal
app=FastAPI()

# Blog. metadata.create_all(engine)
Base.metadata.create_all(engine)

def get_db():
    db =sessionlocal()

    try:
        yield db 
    finally:
        db.close

@app.post("/blog", status_code=status.HTTP_201_CREATED) #here instead of hardcoding it , we can import status and then use it here
def get_blog(request:item , db :Session=Depends(get_db)):
    new_blog=Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return(new_blog)

@app.get("/blog")
def get_All(db :Session=Depends(get_db)):
    blogs=db.query(Blog).all()
    return blogs

@app.get("/blog/{id}")
def retrieve(id:int, db :Session=Depends(get_db)):
    blog= db.query(Blog).filter(Blog.id==id).first()
    return blog

#problem 
# here  the problem is that .. once we create the blog instance , we get response code 200 that should be 201 so we are fixing it for now 
#solution:
# define the status_code in decorator only