from ctypes import Union
from typing import Annotated, Optional
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Payload(BaseModel):
    items: str | None = None
    users: str | None = None

# Example in-memory data (pretending to be a database)
fake_db = {
    "items": [],
    "users": []
}

@app.post("/data", status_code=201)
async def create_data(payload: Annotated[
        Payload, Body(openapi_examples={
                "items": {
                    "summary": "payload to create an item",
                    "description": "Create an item.",
                    "value": {
                        "items": "item1",
                    },
                },
                "users": {
                    "summary": "payload to create an user",
                    "description": "Create an user",
                    "value": {
                        "users": "user1",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "description": "Invalid payload",
                    "value": {
                        "item": 123
                    },
                },
            },
        ),
    ],
):
    """Create data for a specified resource"""
    if payload.items:
        fake_db["items"].append(payload.items)
    elif payload.users:
        fake_db["users"].append(payload.users) 
    else:
        raise HTTPException(status_code=404, detail="Resource not found")   

    return fake_db
