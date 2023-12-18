from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    scan_data = Column(JSONB, default={})


class TimeStampToken(Base):
    __tablename__ = "time_stamp_tokens"

    id = Column(Integer, primary_key=True, index=True)
    tst = Column(LargeBinary)
