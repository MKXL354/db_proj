from fastapi import FastAPI
from models import *
from database_handler import DatabaseHandler

app = FastAPI()
db = DatabaseHandler()


# TODO: read
# TODO: test
# TODO: Add creator to group


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


@app.post("/create_group_member")
def create_group_member(gm: GroupMember):
    return db.create_group_member(gm)


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


@app.delete("/delete_group_member/{group_id}/{user}")
def delete_group_member(group_id: int, user: str):
    return db.delete_group_member(group_id, user)


@app.delete("/delete_msg/{id}")
def delete_msg(id: int):
    return db.delete_msg(id)


@app.delete("/delete_contact/{user1}/{user2}")
def delete_contact(user1: str, user2: str):
    return db.delete_contact(user1, user2)


@app.get("/read_user/{username}")
def read_user(username: str):
    return db.read_user(username)


@app.get("/read_user_contacts/{username}")
def read_user_contacts(username: str):
    return db.read_user_contacts(username)


@app.get("/read_user_chats/{username}")
def read_user_chats(username: str):
    return db.read_user_chats(username)


@app.get("/read_group/{name}")
def read_group(name: str):
    return db.read_group(name)


@app.get("/read_group_members/{name}")
def read_group_members(name: str):
    return db.read_group_members(name)


@app.get("/read_group_messages/{id}")
def read_group_messages(id: int):
    return db.read_group_messages(id)


@app.get("/read_chat_messages/{id}")
def read_chat_messages(id: int):
    return db.read_chat_messages(id)