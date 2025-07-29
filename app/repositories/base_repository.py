import json
from pathlib import Path
from typing import Generic, TypeVar, Type
from pydantic import BaseModel
from app.constants import FILE_ENCODING, READ_MODE

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    def __init__(self, path: str, model: Type[T]):
        self._data = self._load_data(path, model)

    def _load_data(self, path: str, model: Type[T]) -> list[T]:
        file_path = Path(path)
        if not file_path.exists():
            return []
        with file_path.open(READ_MODE, encoding=FILE_ENCODING) as f:
            raw_data = json.load(f)
        return [model(**item) for item in raw_data]

    def get_all(self) -> list[T]:
        return self._data

    def get_by_id(self, id: str) -> T | None:
        return next((obj for obj in self._data if getattr(obj, "id", None) == id), None)
