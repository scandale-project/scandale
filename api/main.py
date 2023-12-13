import sys
from typing import Any
from typing import Dict
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
from pumpkin import __version__

app = FastAPI()


def custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SCANDALE - Pumpkin",
        version="0.1.0",
        summary="API of the Pumpkin project.",
        description="Backend API for collecting data from probes and storing proof of checks from various scans.",
        contact={
            "name": "Computer Incident Response Center Luxembourg",
            "url": "https://www.circl.lu",
            "email": "info@circl.lu",
        },
        license_info={
            "name": "GNU Affero General Public License v3.0 or later",
            "identifier": "AGPL-3.0-or-later",
            "url": "https://www.gnu.org/licenses/agpl-3.0.en.html",
        },
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
def read_item(item_id: int = 0, db: Session = db_session) -> schemas.ItemBase:
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.post("/items/", response_model=schemas.ItemBase)
async def create_item(item: schemas.ItemCreate, db: Session = db_session):
    """Insert a new item."""
    return crud.create_item(db=db, item=item)


@app.get("/system/stats/")
async def stats(db: Session = db_session):
    """Provides stats about the database."""
    return {"dbsize": crud.db_stats(db=db)}


@app.get("/system/info/")
async def system_info():
    """Provides stats and information about the instance."""
    version = __version__.split("-")
    if len(version) == 1:
        software_version = version[0]
        version_url = f"https://github.com/scandale-project/pumpkin/tags/{version[0]}"
    else:
        software_version = f"{version[0]} - {version[2][1:]}"
        version_url = "https://github.com/scandale-project/pumpkin/commit/{}".format(
            version[2][1:]
        )
    return {
        "python_version": "{}.{}.{}".format(*sys.version_info[:3]),
        "version": software_version,
        "version_url": version_url,
    }
