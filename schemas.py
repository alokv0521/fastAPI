from pydantic import BaseModel

class item(BaseModel):
    title: str
    body: str  # ✅ must match your Blog model
