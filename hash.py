from passlib.context import CryptContext




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    @staticmethod
    def bcrypt(password:str):
        return pwd_context.hash(password)
    # @staticmethod
    def verify(plain_pass, hashed_pass):
        return pwd_context.verify(plain_pass, hashed_pass)

