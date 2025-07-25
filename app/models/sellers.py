from pydantic import BaseModel
from typing import Optional

class Seller(BaseModel):
    user_id: str
    reputation: float
    store_name: Optional[str] = None
