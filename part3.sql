create view user_message as
    select *
    from users u left join messages msg on u.username = msg.sender;

create view user_contacts as
    select u1.name as u1_name, u1.family as u1_family, u2.name as u2_name, u2.family as u2_family
    from users u1 join contacts c on u1.username = c.user1 join users u2 on c.user2 = u2.username;

create view group_message_user as
    select u.name, u.family, gm.group_id as id_of_group, msg.*
    from users u join group_members gm on u.username = gm.user join messages msg on u.username = msg.sender
                                                                                        and msg.group_id = gm.group_id;