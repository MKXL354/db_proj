from database_handler import DatabaseHandler
from models import *


class InitialData:

    def __init__(self):
        self.db = DatabaseHandler()

    def create_users(self):
        users = []
        for i in range(10):
            user = User(username=f"u{i}", name=f"n{i}", family=f"f{i}", password=f"p{i}", phonenumber=999123456780 + i)
            users.append(user)
            self.db.create_user(user)
        return users

    def create_groups(self):
        groups = []
        for i in range(2):
            group = MsgGroup(id=i+1, name=f"g{i}")
            groups.append(group)
            self.db.create_group(group)
        return groups

    def create_chat(self):
        chats = []
        for i in range(3):
            chat = Chat(id=i+1, user1=f"u{i}", user2=f"u{i+1}")
            chats.append(chat)
            self.db.create_chat(chat)
        return chats

    def add_to_group(self, msg_group: MsgGroup, user: User):
        gm = GroupMember(group_id=msg_group.id, user=user.username)
        self.db.create_group_member(gm)

    def add_to_contacts(self, user1: User, user2: User):
        contact = Contact(user1=user1.username, user2=user2.username)
        self.db.create_contact(contact)

    def create_message(self, chat, msg_group, user: User, time: datetime,
                       text: str):
        if chat == 0:
            msg = Message(id=0, chat_id=0, group_id=msg_group.id, sender=user.username, time=time, text=text)
        else:
            msg = Message(id=0, chat_id=chat.id, group_id=0, sender=user.username, time=time, text=text)
        self.db.create_msg(msg)


if __name__ == "__main__":
    init = InitialData()
    users = init.create_users()
    groups = init.create_groups()
    chats = init.create_chat()
    for i in range(2):
        for j in range(3):
            init.add_to_group(groups[i], users[3 * i + j])
            # init.create_message(0, groups[i], users[i], datetime.now(), f"from u{i} to g{i} added u{3 * i + j}")
    for i in range(2):
        for j in range(4):
            init.add_to_contacts(users[5 * i], users[5 * i + j + 1])
    for i in range(2):
        # init.create_message(chats[i], 0, users[i], datetime.now(), f"from u{i} to u{i+1}")
        pass
