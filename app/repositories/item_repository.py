import json
from pathlib import Path
from typing import Optional, List
from app.models.item import Item
from app.constants import ITEMS_FILE
from app.constants import FILE_ENCODING, READ_MODE
DATA_FILE = Path(ITEMS_FILE)

class ItemRepository:
    @staticmethod
    def load_all() -> List[Item]:
        if not DATA_FILE.exists():
            return []
        with open(DATA_FILE, READ_MODE, encoding=FILE_ENCODING) as f:
            items_raw = json.load(f)
        return [Item(**item) for item in items_raw]

    @staticmethod
    def get_by_id(item_id: str) -> Optional[Item]:
        items = ItemRepository.load_all()
        return next((item for item in items if item.id == item_id), None)
