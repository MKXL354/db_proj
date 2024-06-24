create table users(
    username varchar(20),
    name varchar(20) not null,
    family varchar(20) not null,
    password varchar(20) not null,
    phone_number char(12) not null,
    primary key(username),
    unique(phone_number),
    constraint chk_phone_number check (phone_number regexp '^[0-9]{12}$')
);

create table contacts(
    user1 varchar(20),
    user2 varchar(20),
    primary key(user1, user2),
    foreign key (user1) references users(username) on delete cascade,
    foreign key (user2) references users(username) on delete cascade
);

create table chats(
    id int auto_increment,
    user1 varchar(20) not null,
    user2 varchar(20) not null,
    primary key(id),
    unique(user1, user2),
    foreign key (user1) references users(username) on delete cascade,
    foreign key (user2) references users(username) on delete cascade
);

create table msg_groups(
    id int auto_increment,
    name varchar(20) not null,
    primary key(id)
);

create table group_members(
    group_id int,
    user varchar(20),
    primary key (group_id, user),
    foreign key (group_id) references msg_groups(id) on delete cascade,
    foreign key (user) references users(username) on delete cascade
);

create table messages(
    id int auto_increment,
    chat_id int,
    group_id int,
    sender varchar(20) not null,
    time datetime not null,
    text varchar(255),
    primary key(id),
    foreign key (chat_id) references chats(id) on delete cascade,
    foreign key (group_id) references msg_groups(id) on delete cascade,
    foreign key (sender) references users(username) on delete cascade,
    constraint belonging check((group_id is not null and chat_id is null) or (group_id is null and chat_id is not null))
);

create table login_dates(
    user varchar(20) not null,
    time datetime not null,
    primary key(user, time),
    foreign key (user) references users(username)
);