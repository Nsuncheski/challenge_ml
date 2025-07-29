from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: str
    title: str
    description: str
    price: float
    seller_id: str


class SellerInfo(BaseModel):
    id: str
    name: str
    email: str
    reputation: float
    store_name: Optional[str] = None


class ItemWithSeller(BaseModel):
    id: str
    title: str
    description: str
    price: float
    seller: SellerInfo
