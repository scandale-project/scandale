from pydantic import BaseModel


class Payload(BaseModel):
    row: str


class Meta(BaseModel):
    uuid: str
    ts: str
    type: str


class ScanData(BaseModel):
    version: str
    format: str
    meta: Meta
    payload: Payload


class ItemBase(BaseModel):
    id: int
    scan_data: ScanData

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass
