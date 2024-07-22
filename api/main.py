import sys
from ast import literal_eval
from typing import Any
from typing import Dict
from typing import List

import rfc3161ng
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import Response
from fastapi import status
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from fastapi_websocket_pubsub import PubSubEndpoint
from sqlalchemy.orm import Session

from . import crud
from . import models
from . import schemas
from .database import engine
from .database import SessionLocal
from scandale import __version__

try:
    from instance import config
except Exception:
    from instance import example as config

security = HTTPBasic()

# app = FastAPI(dependencies=[Depends(security)])
app = FastAPI()

http_security = Depends(security)


def verification(creds: HTTPBasicCredentials = http_security):
    """Verify the credentials via HTTP Basic Authentication method."""
    if not config.AUTHENTICATION_REQUIRED:
        return True
    username = creds.username
    password = creds.password
    if username in config.USERS and password == config.USERS[username]["password"]:
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


# Registers the WebSocket endpoint.
# New scans sent to the HTTP API /items/ endpoint are published via the WebSocket.
pubsub_endpoint = PubSubEndpoint()
pubsub_endpoint.register_route(app, path="/pubsub")


class RawResponse(Response):
    media_type = "binary/octet-stream"

    def render(self, content: bytes) -> bytes:
        return bytes([b ^ 0x54 for b in content])


def custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SCANDALE",
        version="0.1.0",
        summary="API of the SCANDALE project.",
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
auth_verification = Depends(verification)


#
# Item
#


@app.get("/items/", response_model=list[schemas.ItemBase])
def read_items(
    skip: int = 0,
    limit: int = 100,
    q: str = "",
    db: Session = db_session,
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
async def create_item(
    item: schemas.ScanDataCreate,
    db: Session = db_session,
    Verifcation=auth_verification,
):
    """Insert a new item and publish it through the WebSocket."""
    new_item = crud.create_item(db=db, item=item)
    await pubsub_endpoint.publish(["scan"], data=item)
    return new_item


#
# TimeStampToken
#


@app.post("/TimeStampTokens/")
async def create_tst(
    request: Request, db: Session = db_session, Verifcation=auth_verification
):
    """Insert a TimeStampToken and publish it through the WebSocket."""
    data: bytes = await request.body()
    dict_data = literal_eval(data.decode("utf-8"))
    new_tst = crud.create_tst(db=db, data=dict_data)
    dict_tst = {
        "tst": new_tst.tst,
        "scan_uuid": new_tst.scan_uuid,
    }
    dict_tst = str(dict_tst)
    await pubsub_endpoint.publish(["tst"], data=dict_tst)
    return dict_tst


@app.get("/TimeStampTokens/")
def read_tsts(skip: int = 0, limit: int = 100, db: Session = db_session):
    tsts = crud.get_tst(db, skip=skip, limit=limit)
    return str([{"tst": elem.tst, "scan_uuid": elem.scan_uuid} for elem in tsts])


@app.get("/TimeStampTokens/{scan_uuid}", response_model=bytes)
def get_tst(scan_uuid="", db: Session = db_session):
    """Returns a TimeStampToken object corresponding to the scan UUID given as parameter."""
    db_tst = crud.get_tst(db, scan_uuid=scan_uuid)
    if db_tst is None:
        raise HTTPException(status_code=404, detail="TimeStampToken not found")
    return str(
        {
            "tst": db_tst.tst,
            "scan_uuid": db_tst.scan_uuid,
        }
    )


@app.get("/TimeStampTokens/token/{scan_uuid}", response_model=bytes)
def get_tst_token(scan_uuid="", db: Session = db_session):
    """Returns directly the TST as a raw binary stream corresponding to the scan UUID given as parameter."""
    db_tst = crud.get_tst(db, scan_uuid=scan_uuid)
    if db_tst is None:
        raise HTTPException(status_code=404, detail="TimeStampToken not found")
    return RawResponse(content=db_tst.tst)


@app.get("/TimeStampTokens/check/{scan_uuid}")
def check_tst(scan_uuid="", db: Session = db_session):
    """Performs an offline check of a TimeStampToken."""
    db_tst = crud.get_tst(db, scan_uuid=scan_uuid)
    if db_tst is None:
        raise HTTPException(status_code=404, detail="TimeStampToken not found")
    db_item = crud.get_items(db, scan_uuid=scan_uuid)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    certificate = open(config.CERTIFICATE_FILE, "rb").read()
    rt = rfc3161ng.RemoteTimestamper(config.REMOTE_TIMESTAMPER, certificate=certificate)
    result = rt.check(
        db_tst.tst, data=db_item[0].scan_data["payload"]["raw"].encode("utf-8")
    )
    return {"validity": result}


@app.get("/TimeStampTokens/get_timestamp/{scan_uuid}")
def get_timestamp(scan_uuid="", db: Session = db_session):
    """Get the timestamp of a check based on the corresponding TimeStampToken object."""
    db_tst = crud.get_tst(db, scan_uuid=scan_uuid)
    if db_tst is None:
        raise HTTPException(status_code=404, detail="TimeStampToken not found")
    return {"timestamp": rfc3161ng.get_timestamp(db_tst.tst)}


#
# System
#


@app.get("/system/stats/")
async def stats(db: Session = db_session):
    """Provides stats about the database."""
    return {"dbsize": crud.db_stats(db=db)}


@app.get("/system/info/")
def system_info():
    """Provides information about the instance."""
    version = __version__.split("-")
    if len(version) == 1:
        software_version = version[0]
        version_url = f"https://github.com/scandale-project/scandale/tags/{version[0]}"
    else:
        software_version = f"{version[0]} - {version[2][1:]}"
        version_url = "https://github.com/scandale-project/scandale/commit/{}".format(
            version[2][1:]
        )
    return {
        "python_version": "{}.{}.{}".format(*sys.version_info[:3]),
        "version": software_version,
        "version_url": version_url,
    }
