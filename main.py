from fastapi import FastAPI
from models import *
from databaseHandler import DatabaseHandler

app = FastAPI()
db = DatabaseHandler()


@app.post("/create_user")
def create_user(user: User):
    db.create_user(user)
    return user


@app.post("/create_chat")
def create_chat(chat: Chat):
    db.create_chat(chat)
    return chat


@app.post("/create_group")
def create_group(msg_group: MsgGroup):
    db.create_group(msg_group)
    return msg_group
