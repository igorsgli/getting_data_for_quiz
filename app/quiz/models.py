from sqlalchemy import Column, Date, Integer, String
from app.database import Base


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    airdate = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False)
    id_source = Column(Integer, nullable=False)
