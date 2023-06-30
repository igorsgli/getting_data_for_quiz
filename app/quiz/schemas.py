from datetime import date
from pydantic import BaseModel


class Item(BaseModel):
    questions_num: int


class SQuiz(BaseModel):
    id: int
    question: str
    answer: str
    airdate: date
    created_at: date
    id_source: int

    class Config:
        orm_mode = True
