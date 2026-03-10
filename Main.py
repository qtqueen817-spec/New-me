from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Marketplace AI Backend")

# Data Model for a Marketplace Item
class Item(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    price: float
    category: str

# In-memory database for prototyping
inventory = []

@app.get("/")
async def root():
    return {"message": "Welcome to the Marketplace AI API"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return inventory

@app.post("/items")
async def create_item(item: Item):
    item.id = len(inventory) + 1
    inventory.append(item)
    return {"message": "Item listed successfully", "item": item}

@app.post("/predict-price")
async def predict_price(description: str):
    # This is where your AI model logic will eventually live
    # For now, we return a mock suggested price
    suggested_price = len(description) * 0.5  # Mock logic
    return {
        "description_analyzed": description,
        "suggested_price": max(5.0, suggested_price),
        "currency": "USD"
    }
