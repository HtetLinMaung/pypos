
from ..database import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
import uuid


class Category(Base):
    __tablename__ = "category"

    id = Column(String, nullable=False, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))
