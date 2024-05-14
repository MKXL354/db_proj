from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from DatabaseHandler import DatabaseHandler


class User(BaseModel):
    username: str
    name: str
    family: str
    password: str
    phonenumber: int


class Contact(BaseModel):
    user1: str
    user2: str


class Chat(BaseModel):
    id: int
    user1: str
    user2: str


class MsgGroup(BaseModel):
    id: int
    name: str


class Message(BaseModel):
    id: int
    chat_id: int
    group_id: int
    sender: str
    time: datetime
    text: str


if __name__ == "__main__":
    app = FastAPI()
    db = DatabaseHandler()


    @app.post("/create_table")
    def root(table: Table):
        print(table)
        db.create_table(table.name, table.attr)
        return table