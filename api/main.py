from typing import Union, Dict

import redis
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

r = redis.Redis(host='localhost', port=6666, db=0)


class Item(BaseModel):
    version: str
    format: str
    meta: Union[Dict, None] = None
    payload: Union[Dict, None] = None


@app.get("/items/{base64_payload}")
def read_item(base64_payload: str, q: Union[str, None] = None):
    if q:
        item = r.ft().search(q)
    else:
        item = r.get(base64_payload)
    return {"item": item, "q": q}


@app.post("/items/")
def insert_item(item: Item):
    """Insert a new item."""
    return {"item_payload": item.payload}
