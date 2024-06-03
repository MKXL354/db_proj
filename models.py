from typing import Optional

from pydantic import BaseModel
from datetime import datetime


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


class GroupMember(BaseModel):
    group_id: int
    user: str


class Message(BaseModel):
    id: int
    chat_id: Optional[int] = None
    group_id: Optional[int] = None
    sender: str
    time: datetime
    text: str
