import httpx

from datetime import datetime

from app.config import settings
from app.quiz.dao import QuizDAO


async def get_data(questions_num: int):
    async with httpx.AsyncClient() as client:
        url = settings.QUIZ_URL
        params = {'count': questions_num}
        try:
            response = await client.request(
                'GET', url=url, params=params, timeout=60
            )
            response_list = response.json()
        except Exception as err:
            print(
                'Exception при обращении к API!', response.text, err
            )
            return []

        records = []
        for item in response_list:
            records.append(
                {
                    'question': item['question'],
                    'answer': item['answer'],
                    'airdate': datetime.strptime(
                        item['airdate'], '%Y-%m-%dT%H:%M:%S.%f%z'
                    ).date(),
                    'created_at': datetime.strptime(
                        item['created_at'], '%Y-%m-%dT%H:%M:%S.%f%z'
                    ).date(),
                    'id_source': item['id'],
                }
            )
        return records


async def get_data_saved(questions_num: int):
    while questions_num > 0:
        records = await get_data(questions_num)
        if records:
            count_saved_records = (
                await QuizDAO.add_not_repeated(records)
            )
            questions_num -= count_saved_records
