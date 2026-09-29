from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# 1. Define data structures (schemas)
class Item(BaseModel):
    name: str
    price: float

# 2. Instantiate the router (acting as your controller)
router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

# Mock database
DB = {}

# 3. Define action endpoints
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    item_id = len(DB) + 1
    DB[item_id] = item
    return {"id": item_id, **item.model_dump()}

@router.get("/{item_id}")
async def get_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    return DB[item_id]
