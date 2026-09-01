from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

class Item(BaseModel):
    text: str
    is_done: bool = False

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

items = []

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]