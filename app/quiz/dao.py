from app.dao.base import BaseDAO
from app.quiz.models import Quiz


class QuizDAO(BaseDAO):
    model = Quiz
