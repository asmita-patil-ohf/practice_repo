from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    text:str 
    is_done:bool = False

items=[]

@app.get("/")
def root():
    return items

@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model = Item)
def get_item(item_id:int)->Item:
    if item_id < len(items):
        item=items[item_id]
        return item
    else:
        raise HTTPException (status_code=404, detail="Item not found")
    
@app.get("/items", response_model=list[Item])
def list_items(limit:int=10):
    return items[0:limit]