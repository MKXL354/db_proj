from database_handler import DatabaseHandler
from models import *


class InitialData:

    def __init__(self):
        self.db = DatabaseHandler()

    def create_users(self):
        users = []
        for i in range(1, 11, 1):
            user = User(username=f"u{i}", name=f"n{i}", family=f"f{i}", password=f"p{i}", phone_number=f"99912345678{i-1}")
            users.append(user)
            self.db.create_user(user)
        return users

    def create_groups(self):
        groups = []
        for i in range(1, 3, 1):
            group = MsgGroup(id=i, name=f"g{i}")
            groups.append(group)
            self.db.create_group(group)
        return groups

    def create_chat(self):
        chats = []
        for i in range(1, 4, 1):
            chat = Chat(id=i, user1=f"u{i+1}", user2=f"u{i+2}")
            chats.append(chat)
            self.db.create_chat(chat)
        return chats

    def add_to_group(self, msg_group: MsgGroup, user: User):
        gm = GroupMember(group_id=msg_group.id, user=user.username)
        self.db.create_group_member(gm)

    def add_to_contacts(self, user1: User, user2: User):
        contact = Contact(user1=user1.username, user2=user2.username)
        self.db.create_contact(contact)

    def create_message(self, chat, msg_group, user: User, time: datetime, text: str):
        if chat is None:
            msg = Message(id=0, chat_id=None, group_id=msg_group.id, sender=user.username, time=time, text=text)
        else:
            msg = Message(id=0, chat_id=chat.id, group_id=None, sender=user.username, time=time, text=text)
        self.db.create_msg(msg)


if __name__ == "__main__":
    init = InitialData()
    users = init.create_users()
    groups = init.create_groups()
    chats = init.create_chat()
    init.add_to_group(groups[1], users[0])
    init.add_to_group(groups[1], users[1])
    for i in range(2):
        for j in range(3):
            init.add_to_group(groups[i], users[3 * i + j])
    for i in range(2):
        for j in range(4):
            init.add_to_contacts(users[5 * i], users[5 * i + j + 1])
    for i in range(3):
        init.create_message(None, groups[0], users[0], datetime.now(), f"from u1 to g1 number {i}")
        init.create_message(None, groups[1], users[0], datetime.now(), f"from u1 to g2 number {i}")
        init.create_message(None, groups[0], users[1], datetime.now(), f"from u2 to g1 number {i}")
        init.create_message(None, groups[0], users[1], datetime.now(), f"from u2 to g2 number {i}")
        init.create_message(chats[i], None, users[i+1], datetime.now(), f"from u{i+2} to u{i+3}")