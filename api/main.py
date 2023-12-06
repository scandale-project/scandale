from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{payload}")
def read_item(payload: str, q: Union[str, None] = None):
    return {"item_id": payload, "q": q}
