create table if not exists users(
    username varchar(20),
    name varchar(20) not null,
    family varchar(20) not null,
    password varchar(20) not null,
    phonenumber numeric(12, 0) not null,
    primary key(username),
    unique(phonenumber)
);

create table if not exists contacts(
    user1 varchar(20),
    user2 varchar(20),
    primary key(user1, user2),
    foreign key (user1) references users(username),
    foreign key (user2) references users(username)
);

create table if not exists chats(
    id int auto_increment,
    user1 varchar(20) not null,
    user2 varchar(20) not null,
    primary key(id),
    foreign key (user1) references users(username),
    foreign key (user2) references users(username)
);

create table if not exists msg_groups(
    id int auto_increment,
    name varchar(20) not null,
    primary key(id)
);

create table if not exists messages(
    id int auto_increment,
    chat_id int,
    group_id int,
    sender varchar(20) not null,
    time datetime not null,
    text varchar(255),
    primary key(id),
    foreign key (chat_id) references chats(id),
    foreign key (group_id) references msg_groups(id),
    foreign key (sender) references users(username),
    constraint belongs check((group_id is not null and chat_id is null) or (group_id is null and chat_id is not null))
);