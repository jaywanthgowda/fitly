from sqlalchemy import Column, String, UUID, ForeignKey, Integer, Float
from app.db.session import Base
from datetime import datetime, timezone
import uuid

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    title = Column(String, nullable=False)
    description = Column(String)
    date = Column(String, default=datetime.now(timezone.utc).strftime('%Y-%m-%d'))
    duration_minutes = Column(Integer)
    created_at = Column(String, default=datetime.now(timezone.utc), nullable=False)