from fastapi import FastAPI
from models import *
from database_handler import DatabaseHandler

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


@app.post("/create_msg")
def create_msg(msg: Message):
    db.create_msg(msg)
    return msg


@app.post("/create_msg")
def create_contact(contact: Contact):
    db.create_contact(contact)
    return contact


@app.post("/update_user")
def update_user(user: User):
    db.update_user(user)
    return user


@app.post("/update_group")
def update_group(msg_group: MsgGroup):
    db.update_group(msg_group)
    return msg_group


@app.post("/update_msg")
def update_msg(msg: Message):
    db.update_msg(msg)
    return msg
