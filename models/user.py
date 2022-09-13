
from ..database import Base
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
import uuid


class User(Base):
    __tablename__ = "user"

    id = Column(String, nullable=False, primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    profile_image = Column(Text, default="")
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))
