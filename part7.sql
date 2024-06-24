create function count_messages_between_users(user1_id varchar(20), user2_id varchar(20)) returns int reads sql data
    begin
        declare msg_count int;
        select count(msg.id) into msg_count
        from messages msg, (select id
            from chats
            where (user1 = user1_id and user2 = user2_id) or (user2 = user1_id and user1 = user2_id)) as chat_ids
        where msg.chat_id = chat_ids.id;
        return msg_count;
    end;

# MySQL does not support functions that return a table so I used procedure here.
create procedure get_recent_active_users()
    begin
        select distinct user
        from login_dates
        where time >= now() - interval 1 day;
    end;

# MySQL does not support functions that return a table so I used procedure here.
create procedure get_conversation_history(user1_id varchar(20), user2_id varchar(20), max_count int)
    begin
        select msg.*
        from messages msg, (select id
            from chats
            where (user1 = user1_id and user2 = user2_id) or (user2 = user1_id and user1 = user2_id)) as chat_ids
        where msg.chat_id = chat_ids.id
        limit max_count;
    end;

# MySQL does not support functions that return a table so I used procedure here.
create procedure search_messages(keyword text)
    begin
        select *
        from messages
        where text like concat('%', keyword, '%');
    end;