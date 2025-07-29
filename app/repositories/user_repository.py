from app.repositories.base_repository import BaseRepository
from app.models.users import User
from app.constants import USERS_FILE


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(USERS_FILE, User)
