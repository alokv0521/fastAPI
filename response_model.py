from fastapi import FastAPI
from database import engine, Base
from routers import user, blog, authentication
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication.auth)
app.include_router(blog.alok)
app.include_router(user.nilesh)



# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["General"]) 
# def get_blog(request:item , db :Session=Depends(get_db)):
#     new_blog=Blog(title=request.title, body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return(new_blog)

# @app.get("/blog", response_model=List[getAll], tags=["General"]) # here need to return list of blogs .. so it needs to bein list
# def get_All(db :Session=Depends(get_db)):
#     blogs=db.query(Blog).all()
#     return blogs

# @app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=show, tags=["General"])
# def retrieve(id:int, db :Session=Depends(get_db)):
#     blog= db.query(Blog).filter(Blog.id==id).first()
#     if blog :
#         return blog
#     else : 
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"there is no blog containing for the id: {id}"
#         )


# @app.delete("/blog/{id}", tags=["General"])
# def astroid_destroyer(id, db :Session=Depends(get_db)):

#     blog = db.query(Blog).filter(Blog.id==id).first()
#     if not blog :
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the blog with the id: {id} not exist ")
#     else:
#         db.query(Blog).filter(Blog.id==id).delete(synchronize_session=False)
#     db.commit()
#     raise HTTPException( status_code=status.HTTP_200_OK, detail= f"blog with the id:{id} got suscessfully deleted 🤗")


  
# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["General"])
# def update(id,request:item, db :Session=Depends(get_db)):
#     db.query(Blog).filter(Blog.id==id).update({"title":request.title, "body":request.body}, synchronize_session=False )  
#     db.commit()
#     return {"suscessfully updated the record having id: {id}"}


# # ok so as of now we have returened the reponse ... but what if we need that in some specific format and don't need everything 
# # for that purpose , we will define another schema and hence concept of response model is there
# # siply put the parameter reponse_model=model name in decorator 
# # and that model will be none other than pydantic schema hence we need to decalre one more schema in the original schema
# # here we have two types of model , pydantic and sqlalchamy , sql one is called model whileas pydantic is called schema ,.. hence here we mean  response schema  by response_model

# # now we are creating user using post method
# # @app.post("/user")
# # def user(request:use, db :Session=Depends(get_db)):
# #     # hash_pass=pwd_context.hash(request.password)
# #     new_user=User(name=request.name, email=request.email, password=hash.bcrypt(request.password))
# #     db.add(new_user)
# #     db.commit()
# #     db.refresh(new_user)
# #     return(new_user)

# # now the above code is returning the pass as response that we don't want 
# @app.post("/user", response_model=user_incrypted, tags=["User"])
# def user(request:use, db :Session=Depends(get_db)):
#     # hash_pass=pwd_context.hash(request.password)
#     new_user=User(name=request.name, email=request.email, password=hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return(new_user)

# @app.get("/user/{id}", response_model=user_incrypted, status_code=status.HTTP_200_OK, tags=["User"])
# def retrieve_user(id:int, db :Session=Depends(get_db)):
#     new_user=db.query(User).filter(User.id==id).first()
#     if new_user:
#         return new_user
#     else:
#         raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f"the user with the id:{id} is not found")
    






# Allow origins (e.g., localhost:3000 for React, or "*")
origins = [
    "http://localhost:3000",  # Frontend URL
    "http://127.0.0.1:3000",  # Alternative localhost
    "*"  # <-- Allow all (not safe for production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # <- origins list
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)