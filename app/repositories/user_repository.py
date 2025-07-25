import json
from pathlib import Path
from typing import Optional, List
from app.models.user import User
from app.constants import USERS_FILE
from app.constants import FILE_ENCODING, READ_MODE
DATA_FILE = Path(USERS_FILE)

class UserRepository:
    @staticmethod
    def load_all() -> List[User]:
        if not DATA_FILE.exists():
            return []
        with open(DATA_FILE, READ_MODE, encoding=FILE_ENCODING) as f:
            users_raw = json.load(f)
        return [User(**user) for user in users_raw]

    @staticmethod
    def get_by_id(user_id: str) -> Optional[User]:
        users = UserRepository.load_all()
        return next((user for user in users if user.id == user_id), None)
