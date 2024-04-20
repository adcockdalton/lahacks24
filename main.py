from fastapi import FastAPI

from functions.answer import storeAnswer
from functions.test import storeValue, getQuestion

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/setUser")
async def setUser(parameter: dict):
    return {"uuid": storeValue(parameter)}

@app.get("/question")
async def question():
    return getQuestion()


@app.get("/setAnswer")
async def setAnswer(uuid: str, answer: str):
    storeAnswer(uuid, answer)
    return {"message": "Done"}

