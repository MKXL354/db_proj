import mysql.connector
from models import *

class DatabaseHandler:
    def __init__(self):
        self.give_value()
        with open('init.sql', 'r') as file:
            sql_script = file.read()
        self.execute_query(sql_script)

    def give_value(self):
        self.mydb = self.get_connecion()
        self.mycursor = self.mydb.cursor()

    def get_connecion(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_proj"
        )

    # def init_db(self):
    #     with open('init.sql', 'r') as file:
    #         sql_script = file.read()
    #     while (True):
    #         try:
    #             self.mycursor.execute(sql_script, multi=True)
    #
    #             break
    #         except mysql.connector.Error:
    #             self.give_value()


    def execute_query(self, query: str):
        while (True):
            try:
                self.mycursor.execute(query, multi=True)
                # self.mycursor.close()
                # self.mycursor = self.mydb.cursor()
                break
            except mysql.connector.Error as e:
                print(e)
                self.give_value()

    def create_user(self, user: User):
        query = f"INSERT INTO users (username, name, family, password, phonenumber) VALUES ('{user.username}', '{user.name}', '{user.family}', '{user.password}', {user.phonenumber})"
        self.execute_query(query)

    def create_chat(self, chat: Chat):
        query = f"INSERT INTO chats (id, user1, user2) VALUES ({chat.id}, '{chat.user1}', '{chat.user2}')"
        self.execute_query(query)

    def create_group(self, msg_group: MsgGroup):
        query = f"INSERT INTO msg_groups (id, name) VALUES ({msg_group.id}, '{msg_group.name}')"
        self.execute_query(query)