from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.dialects.postgresql import JSONB

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    scan_data = Column(JSONB, default={})
