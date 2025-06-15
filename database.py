# ORM stands for object relational model 
# in which for example you have made a table ... so in order to work with we are required to make a object of it 
# we the object is mapping with relation 

from sqlalchemy import create_engine # to connect to the db
from sqlalchemy.ext.declarative import declarative_base # to make the ORM model
from sqlalchemy.orm import sessionmaker # to create session to intract with the db 

#defining database URL , here we are using some local sqlite db 
SQLALCHAMY_DATABASE_URL="sqlite:///./blog.db"


#creating engine
engine=create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread":False})
#basically fast api is uses multi threaded request ... hence setting check_same_thread will throw some thread related errors ... so put it false to make other threads reuest acess it 

#creating a session
sessionlocal=sessionmaker(bind=engine,  autocommit=False, autoflush=False)

# declare a mapping 
Base=declarative_base()

#now db coneection is created 

# now to create a table in we need to define the fields 
