from fastapi import APIRouter, HTTPException

from app.services.item_service import ItemService
from app.models.items import ItemWithSeller
from app.constants import (
    GET_ITEM_BY_ID_PATH,
    ITEMS_PREFIX,
    ITEMS_TAG,
    ITEM_NOT_FOUND_MSG,
    HTTP_404_NOT_FOUND
)

router = APIRouter(
    prefix=ITEMS_PREFIX,
    tags=[ITEMS_TAG]
)

@router.get(GET_ITEM_BY_ID_PATH, response_model=ItemWithSeller)
def get_item(item_id: str):
    item = ItemService.get_item_with_seller(item_id)
    if item is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=ITEM_NOT_FOUND_MSG)
    return item
