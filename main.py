from fastapi import FastAPI
from models import *
from database_handler import DatabaseHandler

app = FastAPI()
db = DatabaseHandler()


# TODO: correct return for methods (maybe use exceptions)
# TODO: update?, read
# TODO: test
# TODO: user1, user2 in chats table can be user2, user1 (duplicate chat)


@app.post("/create_user")
def create_user(user: User):
    return db.create_user(user)


@app.post("/create_chat")
def create_chat(chat: Chat):
    return db.create_chat(chat)


@app.post("/create_group")
def create_group(msg_group: MsgGroup):
    return db.create_group(msg_group)


@app.post("/create_msg")
def create_msg(msg: Message):
    return db.create_msg(msg)


@app.post("/create_contact")
def create_contact(contact: Contact):
    return db.create_contact(contact)


@app.put("/update_user")
def update_user(user: User):
    return db.update_user(user)


@app.put("/update_group")
def update_group(msg_group: MsgGroup):
    return db.update_group(msg_group)


@app.put("/update_msg")
def update_msg(msg: Message):
    return db.update_msg(msg)


@app.delete("/delete_user/{username}")
def delete_user(username: str):
    return db.delete_user(username)


@app.delete("/delete_chat/{id}")
def delete_chat(id: int):
    return db.delete_chat(id)


@app.delete("/delete_group/{id}")
def delete_group(id: int):
    return db.delete_group(id)


@app.delete("/delete_msg/{id}")
def delete_msg(id: int):
    return db.delete_msg(id)


@app.delete("/delete_msg/{user1}/{user2}")
def delete_contact(user1: str, user2: str):
    return db.delete_contact(user1, user2)
