from sqlalchemy import Column, String, UUID
from app.db.session import Base
from datetime import datetime, timezone
import uuid

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(String,default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(String,default=datetime.now(timezone.utc), nullable=False)