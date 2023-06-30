import asyncio
import math

from fastapi import APIRouter

from app.quiz.dao import QuizDAO
from app.quiz.schemas import SQuiz, Item
from app.quiz.utils import get_data_saved

router = APIRouter(
    prefix='',
    tags=['Quiz questions'],
)


@router.post('/')
async def add_questions(item: Item):
    questions_num = item.questions_num
    pack = 100
    questions_by_pack = (
        [pack] * (questions_num // pack)
        + [questions_num % pack] * (questions_num % pack != 0)
    )

    tasks = [
        get_data_saved(questions_by_pack[i])
        for i in range(math.ceil(questions_num / pack))
    ]
    await asyncio.gather(*tasks)

    return await QuizDAO.get_last_record()


@router.get('/get_all')
async def get_questions() -> list[SQuiz]:
    return await QuizDAO.find_all()
