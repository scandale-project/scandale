from typing import Union, Dict

import redis
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

r = redis.Redis(host='localhost', port=6666, db=0)


class Payload(BaseModel):
    row: str

class Meta(BaseModel):
    uuid: str
    ts: str
    type: str

class Item(BaseModel):
    version: str
    format: str
    meta: Meta
    payload: Payload


@app.get("/items/{base64_payload}")
async def read_item(base64_payload: str, q: Union[str, None] = None): # -> Item:
    if q:
        for key in r.scan_iter(f"{q}:*"):
            print(key)
            item = key
    else:
        item = r.get(base64_payload)
    print(item)
    return item


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Insert a new item."""
    res = r.set(item.payload.row, item.model_dump_json())
    # res = r.sadd("items", item.model_dump_json())
    # print(item.payload.row)
    # print(item.model_dump_json())
    print(res)
    return item


@app.get("/stats/")
async def stats():
    """Provides stats about the database."""
    return {"dbsize": r.scard("items")}
