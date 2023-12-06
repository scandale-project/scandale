from typing import Union

import redis
from fastapi import FastAPI

app = FastAPI()

r = redis.Redis(host='localhost', port=6666, db=0)

@app.get("/items/{base64_payload}")
def read_item(base64_payload: str, q: Union[str, None] = None):
    if q:
        item = r.ft().search(q)
    else:
        item = r.get(base64_payload)
    return {"item": item, "q": q}
