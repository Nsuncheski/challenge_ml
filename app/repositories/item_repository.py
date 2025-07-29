from app.repositories.base_repository import BaseRepository
from app.models.items import Item
from app.constants import ITEMS_FILE

class ItemRepository(BaseRepository[Item]):
    def __init__(self):
        super().__init__(ITEMS_FILE, Item)
