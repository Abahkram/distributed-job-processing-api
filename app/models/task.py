from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pending")
    job_type = Column(String, default="report_generation")
    result = Column(String, nullable=True)
