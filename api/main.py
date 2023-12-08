from typing import Union, Dict

import redis
import psycopg2
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

r = redis.Redis(host='localhost', port=6666, db=0)
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="pumpkin",
    user="cedric",
    password="your_password",
    host="127.0.0.1",
    port=""
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define a table in PostgreSQL to store JSON data
table_name = "scan_data"
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, data JSONB)")


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
    # res = r.set(item.payload.row, item.model_dump_json())
    #   res = r.sadd("items", item.model_dump_json())
    # print(item.payload.row)
    # print(item.model_dump_json())
    json_string = json.dumps(item)
    # Insert the JSON data into the PostgreSQL table
    cursor.execute(f"INSERT INTO {table_name} (data) VALUES (%s)", (json_string,))
    # Commit the changes
    conn.commit()
    return item


@app.get("/stats/")
async def stats():
    """Provides stats about the database."""
    return {"dbsize": r.scard("items")}
