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

    def execute_query(self, query: str, is_select):
        res: bool
        query_res = 0
        db = self.con_pool.get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(query)
            if is_select:
                query_res = cursor.fetchall()
            res = True
        except mysql.connector.Error as e:
            print(e)
            res = False
        db.commit()
        cursor.close()
        db.close()

        if not res:
            return "failed"
        else:
            if not is_select:
                return "success"
            else:
                return query_res

    def create_user(self, user: User):
        query = f"insert into users (username, name, family, password, phonenumber) values ('{user.username}'\
, '{user.name}', '{user.family}', '{user.password}', {user.phonenumber})"
        return self.execute_query(query, False)

    def create_chat(self, chat: Chat):
        if chat.user1 > chat.user2:
            user1 = chat.user1
            user2 = chat.user2
        else:
            user1 = chat.user2
            user2 = chat.user1
        query = f"insert into chats (user1, user2) values ('{user1}', '{user2}')"
        return self.execute_query(query, False)

    def create_group(self, msg_group: MsgGroup):
        query = f"insert into msg_groups (name) values ('{msg_group.name}')"
        return self.execute_query(query, False)

    def create_msg(self, msg: Message):
        chat_id = 'NULL' if msg.chat_id is None else msg.chat_id
        group_id = 'NULL' if msg.group_id is None else msg.group_id
        query = f"insert into messages (chat_id, group_id, sender, time, text) values ({chat_id}, {group_id}\
, '{msg.sender}', '{msg.time}', '{msg.text}')"
        return self.execute_query(query, False)

    def create_contact(self, contact: Contact):
        query = f"insert into contacts (user1, user2) values ('{contact.user1}', '{contact.user2}')"
        return self.execute_query(query, False)

    def create_group_member(self, gm: GroupMember):
        query = f"insert into group_members (group_id, user) values ({gm.group_id}, '{gm.user}')"
        return self.execute_query(query, False)

    def update_user(self, user: User):
        query = f"update users set name = '{user.name}', family = '{user.family}', password = '{user.password}'\
, phonenumber = {user.phonenumber} where username = '{user.username}'"
        return self.execute_query(query, False)

    def update_group(self, msg_group: MsgGroup):
        query = f"update msg_groups set name = '{msg_group.name}' where id = {msg_group.id}"
        return self.execute_query(query, False)

    def update_msg(self, msg: Message):
        query = f"update messages set text = '{msg.text}' where id = {msg.id}"
        return self.execute_query(query, False)

    def delete_user(self, username: str):
        query = f"delete from users where username = '{username}'"
        return self.execute_query(query, False)

    def delete_chat(self, id: int):
        query = f"delete from chats where id = {id}"
        return self.execute_query(query, False)

    def delete_group(self, id: int):
        query = f"delete from msg_groups where id = {id}"
        return self.execute_query(query, False)

    def delete_group_member(self, group_id: int, user: str):
        query = f"delete from group_members where group_id = {group_id} and user = '{user}'"
        return self.execute_query(query, False)

    def delete_msg(self, id: int):
        query = f"delete from messages where id = {id}"
        return self.execute_query(query, False)

    def delete_contact(self, user1: str, user2: str):
        query = f"delete from contacts where user1 = '{user1}' and user2 = '{user2}'"
        return self.execute_query(query, False)

    def read_user(self, username: str):
        query = f"select * from users where username = '{username}'"
        return self.execute_query(query, True)

    def read_user_contacts(self, username: str):
        query = f"select * from contacts where user1 = '{username}'"
        return self.execute_query(query, True)

    def read_user_chats(self, username: str):
        query = f"select * from chats where user1 = '{username}' or user2 = '{username}'"
        return self.execute_query(query, True)

    def read_user_groups(self, username: str):
        query = f"select group_id, name from group_members natural join msg_groups where user = '{username}'"
        return self.execute_query(query, True)

    def read_group(self, name: str):
        query = f"select * from msg_groups where name = '{name}'"
        return self.execute_query(query, True)

    def read_group_members(self, name: str):
        query = f"select * from group_members join msg_groups where name = '{name}'"
        return self.execute_query(query, True)

    def read_group_messages(self, id: int):
        query = f"select * from messages where group_id = {id}"
        return self.execute_query(query, True)

    def read_chat_messages(self, id: int):
        query = f"select * from messages where chat_id = {id}"
        return self.execute_query(query, True)
