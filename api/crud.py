from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_items(db: Session, skip: int = 0, limit: int = 100, query: str = ""):
    """Filter items with a query."""
    if query:
        return (
            db.query(models.Item)
            .filter(models.Item.scan_data["payload"]["row"].astext == query)
            .offset(skip)
            .limit(limit)
            .all()
        )
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    """Get an item by id."""
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    """Create an item."""
    db_item = models.Item(scan_data=item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_tst(db: Session, data: schemas.ItemCreate):
    """Create a TimeStampToken."""
    db_tst = models.TimeStampToken(tst=data)
    db.add(db_tst)
    db.commit()
    db.refresh(db_tst)
    return db_tst


def get_tst(db: Session, skip: int = 0, limit: int = 100):
    """Filter TimeStampToken with a query."""
    return db.query(models.TimeStampToken).offset(skip).limit(limit).all()


def db_stats(db: Session):
    return {
        "scans": db.query(models.Item).count(),
        "tst": db.query(models.TimeStampToken).count(),
    }
