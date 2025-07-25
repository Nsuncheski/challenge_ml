from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: str
    title: str
    description: str
    price: float
    seller_id: str
