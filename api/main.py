from typing import Union

import psycopg2
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="pumpkin",
    user="cedric",
    password="password",
    host="127.0.0.1",
    port=5432
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define a table in PostgreSQL to store JSON data
TABLE_NAME = "scan_data"
cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id SERIAL PRIMARY KEY, data JSONB)")


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
    return {}


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Insert a new item."""
    json_string = json.dumps(item)
    # Insert the JSON data into the PostgreSQL table
    cursor.execute(f"INSERT INTO {TABLE_NAME} (data) VALUES (%s)", (json_string,))
    # Commit the changes
    conn.commit()
    return item


@app.get("/stats/")
async def stats():
    """Provides stats about the database."""
    res = cursor.execute(f"select count(*) from {TABLE_NAME};")
    results = cursor.fetchone()
    return {"dbsize": results[0]}
