from typing import List

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session

from . import crud
from . import models
from . import schemas
from .database import engine
from .database import SessionLocal

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SCANDALE - Pumpkin",
        version="0.1.0",
        summary="API of the Pumpkin project.",
        description="Backend API for collecting data from probes and storing proof of checks from various scans.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://www.circl.lu/assets/images/circl-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_session: Session = Depends(get_db)


@app.get("/items/", response_model=list[schemas.ItemBase])
async def read_items(
    skip: int = 0, limit: int = 100, q: str = "", db: Session = db_session
) -> List[schemas.ItemBase]:
    items = crud.get_items(db, skip=skip, limit=limit, query=q)
    return items


@app.get("/items/{item_id}", response_model=schemas.ItemBase)
def read_item(
    item_id: int = 0, q: str = "", db: Session = db_session
) -> schemas.ItemBase:
    db_item = crud.get_item(db, item_id=item_id, query=q)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.post("/items/", response_model=schemas.ItemBase)
async def create_item(item: schemas.ItemCreate, db: Session = db_session):
    """Insert a new item."""
    return crud.create_item(db=db, item=item)


@app.get("/stats/")
async def stats(db: Session = db_session):
    """Provides stats about the database."""
    return {"dbsize": crud.db_stats(db=db)}
