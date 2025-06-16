from passlib.context import CryptContext
from schemas import use



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class hash():
    def bcrypt(password:str):
        return pwd_context.hash(password)

