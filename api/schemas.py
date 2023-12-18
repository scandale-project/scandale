from pydantic import BaseModel


class Payload(BaseModel):
    row: str


class Meta(BaseModel):
    uuid: str
    ts: int
    type: str


class ScanData(BaseModel):
    version: str
    format: str
    meta: Meta
    payload: Payload

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    scan_data: ScanData

    class Config:
        from_attributes = True


class ItemCreate(ItemBase):
    pass


class ScanDataCreate(ScanData):
    pass


class TimeStampToken(BaseModel):
    tst: bytes
