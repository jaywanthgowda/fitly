from sqlalchemy import Column, String, UUID, ForeignKey, Integer, Float
from app.db.session import Base
from datetime import datetime, timezone
import uuid


class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    full_name = Column(String)
    age = Column(Integer)
    height_cm = Column(Float)
    weight_kg = Column(Float)
    gender = Column(String)
    activity_level = Column(String)
    goal = Column(String)
    created_at = Column(String, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(String, default=datetime.now(timezone.utc), nullable=False)