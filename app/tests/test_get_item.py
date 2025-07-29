import pytest

@pytest.mark.asyncio
async def test_get_item_by_id(client):
    item_id = "item1"

    async with client as ac:
        response = await ac.get(f"/items/{item_id}")
    
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == item_id
    assert "title" in data
    assert "price" in data
    assert "seller" in data
    assert "name" in data["seller"]
