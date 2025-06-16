from fastapi import FastAPI, Depends, status, HTTPException
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

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def retrieve(id:int, db :Session=Depends(get_db)):
    blog= db.query(Blog).filter(Blog.id==id).first()
    if blog :
        return blog
    else :
        # status_code=status.HTTP_100_CONTINUE
        # return {f"there is no blog containing for the id: {id}"}
        #you will need to raise a HTTPSException() in order to put custom status code when blog not found 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there is no blog containing for the id: {id}"
        )


@app.delete("/blog/{id}")
def astroid_destroyer(id, db :Session=Depends(get_db)):

    blog = db.query(Blog).filter(Blog.id==id).first()
    if not blog :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the blog with the id: {id} not exist ")
    else:
        db.query(Blog).filter(Blog.id==id).delete(synchronize_session=False) # got deleted but can be seen on get as changes are not commited 
    db.commit()
    raise HTTPException( status_code=status.HTTP_200_OK, detail= f"blog with the id:{id} got suscessfully deleted 🤗")



#put method , this is a bulk method , means if two data having same email ... they both will be updated  
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id,request:item, db :Session=Depends(get_db)):
    db.query(Blog).filter(Blog.id==id).update({"title":request.title, "body":request.body}, synchronize_session=False )
    db.commit()
    return {"suscessfully updated the record having id: {id}"}

        


    

#problem 
# here  the problem is that .. once we create the blog instance , we get response code 200 that should be 201 so we are fixing it for now 
#solution:
# define the status_code in decorator only