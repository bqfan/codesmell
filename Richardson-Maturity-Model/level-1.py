from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Example in-memory data (pretending to be a database)
fake_db = {
    "items": [],
    "users": []
}

@app.post("/items", status_code=201)
async def create_item(payload: dict):
    """Create data for a specified resource"""
    if "items" in payload:
        fake_db["items"].append(payload["items"])
    else:
        raise HTTPException(status_code=404, detail="Resource not found")   

    return {"resource": "items", "item_created": payload["items"]}

@app.post("/users", status_code=201)
async def create_user(payload: dict):
    """Create data for a specified resource"""
    if "users" in payload:
        fake_db["users"].append(payload["users"])
    else:
        raise HTTPException(status_code=404, detail="Resource not found")   

    return {"resource": "users", "user_created": payload["users"]}