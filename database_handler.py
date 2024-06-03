import mysql.connector
from models import *


class DatabaseHandler:
    def __init__(self):
        self.dbconfig = {
            "user": "root",
            "password": "root",
            "host": "localhost",
            "database": "db_proj",
            "raise_on_warnings": True
        }
        self.con_pool = mysql.connector.pooling.MySQLConnectionPool(**self.dbconfig)

    def execute_query(self, query: str):
        db = self.con_pool.get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.Error as e:
            print(e)
        db.commit()
        cursor.close()
        db.close()

    def create_user(self, user: User):
        query = f"insert into users (username, name, family, password, phonenumber) values ('{user.username}', '{user.name}', '{user.family}', '{user.password}', {user.phonenumber})"
        self.execute_query(query)

    def create_chat(self, chat: Chat):
        query = f"insert into chats (user1, user2) values ('{chat.user1}', '{chat.user2}')"
        self.execute_query(query)

    def create_group(self, msg_group: MsgGroup):
        query = f"insert into msg_groups (name) values ('{msg_group.name}')"
        self.execute_query(query)
