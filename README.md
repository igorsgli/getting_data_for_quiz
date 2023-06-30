# Gathering data for quizes / Сбор данных для викторин
Mini service for collecting data for quizzes from the public API https://jservice.io/api/ and saving it to the database. The data for quizzes includes questions, answers, and creation and air dates.
A request with the number of required questions is sent to the service, after which the service requests the specified number of questions from the public API (https://jservice.io/api/random?count=1, where count=1 is the number of questions requested).
The public API returns questions randomly, limited to 100 at a time, which are then stored in the database. If the database already has the same question, then requests to the public API with quizzes are made until a unique question for the quiz is obtained.
***************************
Мини сервис для сбора данных для викторин с публичного API https://jservice.io/api/ и их сохранения в базу данных. Данные для викторин включают в себя вопросы, ответы и даты создания и выхода в эфир. 
На сервис передается запрос с количеством необходимых вопросов, после чего сервис запрашивает с публичного API указанное количество вопросов (https://jservice.io/api/random?count=1, где  count=1 - количество запрашиваемых вопросов). 
Публичный API возвращает вопросы в случайном порядке с ограничением до 100 записей за раз, которые далее сохраняются в базе данных. Если в базе данных уже имеется такой же вопрос, то запросы к публичному API с викторинами выполняются до тех пор, пока не будет получен уникальный вопрос для викторины.

**Stack / Стек**:
* Python
* FastAPI
* asyncio
* PostgresSQL
* SQLAlchemy
* Pydantic
* Gunicorn
* Docker
* Swagger

## Launch the project / Инструкции по запуску

### 1. Git clone / Клонировать репозиторий:
```
git clone https://github.com/igorsgli/test_bewise_1.git
cd test_bewise_1
```
### 2. Install depencies / Установить зависимости:
```
pip install -r requirements.txt
```
### 3. Rename .env_example to .env / Переименовать файл .env_example в .env:
```
mv ./.env_example ./.env
```
### 4. Run docker-compose / Запустить docker-compose:
```
docker-compose up -d --build
```
### 5. Project documentation is available at / Документация доступна по адресу:
```
http://127.0.0.1:8000/docs
```
### 6. API requests examples / Примеры API запросов:
1. Request for getting quis questions from 3rd party site and recording the questions into database. Number of questions is submitted in the POST request body. / Запрос на получение вопросов викторины с внешнего сайта и запись вопросов в базу данных. Количество вопросов передается в теле POST запроса.
```
POST http://127.0.0.1:8000/
{
  "questions_num": 1,
}
```
2. Getting quiz questions list. / Получение списка вопросов викторины.
```
GET http://127.0.0.1:8000/get_all
[
  {
    "id": 0,
    "question": "string",
    "answer": "string",
    "airdate": "2001-05-01",
    "created_at": "2023-05-25",
    "id_source": 0
  }
]
```