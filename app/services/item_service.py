from typing import Optional

from app.models.items import Item, ItemWithSeller, SellerInfo
from app.models.users import User
from app.models.sellers import Seller

from app.repositories.item_repository import ItemRepository
from app.repositories.user_repository import UserRepository
from app.repositories.seller_repository import SellerRepository


class ItemService:
    @staticmethod
    def get_item_with_seller(item_id: str) -> Optional[ItemWithSeller]:
        item: Optional[Item] = ItemRepository().get_by_id(item_id)
        if not item:
            return None

        user: Optional[User] = UserRepository().get_by_id(item.seller_id)
        if not user:
            return None

        seller: Optional[Seller] = SellerRepository().get_by_user_id(user.id)
        if not seller:
            return None

        seller_info = SellerInfo(
            id=user.id,
            name=user.name,
            email=user.email,
            reputation=seller.reputation,
            store_name=seller.store_name,
        )

        return ItemWithSeller(
            id=item.id,
            title=item.title,
            description=item.description,
            price=item.price,
            seller=seller_info,
        )
