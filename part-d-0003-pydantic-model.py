from datetime import date

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    quantity: int = 0 # default value 0
    expiration: date = None # default None
