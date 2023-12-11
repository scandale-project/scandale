from typing import Union

import json
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/", response_model=list[schemas.ItemBase])
async def read_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/items/", response_model=schemas.ItemBase)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Insert a new item."""
    # json_string = json.dumps(item)
    return crud.create_item(db=db, item=item)


@app.get("/stats/")
async def stats():
    """Provides stats about the database."""
    return {"dbsize": 0}
