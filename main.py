from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from functions.answer import storeAnswer
from functions.test import storeValue, getQuestion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

class User(BaseModel):
    name: str
    birthday: str

@app.post("/setUser")
async def setUser(user: User):
    return {"uuid": storeValue(user.name, user.birthday)}


class UUID(BaseModel):
    uuid: str
@app.post("/question")
async def question(u: UUID):
    return {"question": getQuestion(u.uuid)}

class Answer(BaseModel):
    uuid: str
    answer: str

@app.post("/setAnswer")
async def setAnswer(a: Answer):
    storeAnswer(a.uuid, a.answer)
    return {"message": "Done"}

