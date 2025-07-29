from typing import Optional
from app.repositories.base_repository import BaseRepository
from app.models.sellers import Seller
from app.constants import SELLERS_FILE


class SellerRepository(BaseRepository[Seller]):
    def __init__(self):
        super().__init__(SELLERS_FILE, Seller)

    def get_by_user_id(self, user_id: str) -> Optional[Seller]:
        return next((s for s in self._data if s.user_id == user_id), None)
