from fastapi import FastAPI

from app.quiz.router import router as router_quiz

app = FastAPI()

app.include_router(router_quiz)
