from typing import List

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import crud
from . import models
from . import schemas
from .database import engine
from .database import SessionLocal

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
async def read_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[schemas.ItemBase]:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}", response_model=schemas.ItemBase)
def read_item(
    item_id: int = 0, q: str = "", db: Session = Depends(get_db)
) -> schemas.ItemBase:
    db_item = crud.get_item(db, item_id=item_id, query=q)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.post("/items/", response_model=schemas.ItemBase)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Insert a new item."""
    return crud.create_item(db=db, item=item)


@app.get("/stats/")
async def stats(db: Session = Depends(get_db)):
    """Provides stats about the database."""
    return {"dbsize": crud.db_stats(db=db)}
