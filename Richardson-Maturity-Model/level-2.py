from typing import Annotated
from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

# Example in-memory data (pretending to be a database)
fake_db = {
    "items": [],
    "users": []
}

@app.post("/data/items")
async def create_item(payload: Annotated[str, Body(examples=["item1"])]):
    """Create an item in the 'items' resource"""
    fake_db["items"].append(payload)
    return {"resource": "items", "item_created": payload}


@app.get("/data/items")
async def get_items():
    """Get items in the 'items' resource"""
    return {"items": fake_db["items"]}

@app.post("/data/users")
async def create_user(payload: Annotated[str, Body(examples=["user1"])]):
    """Create a user in the 'users' resource"""
    fake_db["users"].append(payload)
    return {"resource": "users", "user_created": payload}

@app.get("/data/users")
async def get_users():
    """Get users in the 'users' resource"""
    return { "users": fake_db["users"]}