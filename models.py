from sqlalchemy import Column , Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from database import sessionlocal


# class Blog (Base):
#     __tablename__="Blogs"

#     id=Column(Integer, primary_key=True, index=True)
#     title=Column(String)
#     body =Column(String)

#     #we will define a foreign key here
#     User_id=Column(Integer, ForeignKey("User.id"))

#     #we will define a relationship 
#     owner=relationship("User", back_populates="Blogs") # here these two are table names (Users and Blogs)

#     # as we have make relationship , we need to make it in other table also




# # now we have created this model ... so how we can use this model 

# class User(Base):
#     __tablename__="User"

#     id=Column(Integer, primary_key=True, index=True)
#     name=Column(String)
#     email=Column(String)
#     password=Column(String)

#     blog=relationship("Blogs", back_populates="owner")

class Blog(Base):
    __tablename__ = "Blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("User.id"))

    owner = relationship("User", back_populates="blogs")  # ✅ match 'blogs' in User


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="owner")  # ✅ match 'owner' in Blog


def get_db():
    db =sessionlocal()

    try:
        yield db 
    finally:
        db.close