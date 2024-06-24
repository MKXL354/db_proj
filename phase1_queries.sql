insert into users values ('t', 'Tom', 'Kane', 'tk', '044796268462');
insert into group_members values (1, 't');
insert into messages values (0, null, 1, 't', '2024/06/03 20:20:20', 'Hello this is Tom');
update users set phone_number = '447342780080' where username = 't';

# Query 1
select u.*, gm.group_id
from users u join group_members gm on u.username = gm.user;

# Query 2
select u.*, count(m.id) as message_count
from users u join messages m on u.username = m.sender
where m.group_id = 2
group by u.username
order by message_count desc;

# Query 3
select g.*, count(c.id) as private_chat_count
from chats as c, msg_groups as g
where (g.id, c.user1, c.user2) in (select g1.group_id, g1.user, g2.user
                             from group_members g1 join group_members g2 on g1.group_id = g2.group_id
                             where g1.user <> g2.user)
group by g.id;

# Query 4
select sender
from (select sender, group_id
    from messages
    where date(time) = '2024-06-24' and group_id is not null
    group by sender, group_id
    having count(group_id) > 1) as count_table join login_dates on user = sender
where date(time) = '2024-06-24'
group by sender
having count(count_table.group_id) >= 2;

# Query 5
select u.*
from users u join group_members gm on u.username = gm.user
where u.username <> 'u0' and gm.group_id in (select group_id
                      from group_members
                      where user = 'u0');
