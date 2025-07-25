import json
from pathlib import Path
from typing import Optional, List
from app.models.seller import Seller
from app.constants import SELLERS_FILE
from app.constants import FILE_ENCODING, READ_MODE
DATA_FILE = Path(SELLERS_FILE)

class SellerRepository:
    @staticmethod
    def load_all() -> List[Seller]:
        if not DATA_FILE.exists():
            return []
        with open(DATA_FILE, READ_MODE, encoding=FILE_ENCODING) as f:
            sellers_raw = json.load(f)
        return [Seller(**seller) for seller in sellers_raw]

    @staticmethod
    def get_by_user_id(user_id: str) -> Optional[Seller]:
        sellers = SellerRepository.load_all()
        return next((seller for seller in sellers if seller.user_id == user_id), None)
