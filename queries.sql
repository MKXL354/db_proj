INSERT INTO users VALUES ('t', 'Tom', 'Kane', 'tk', 44796268462);
INSERT INTO group_members VALUES (1, 't');
INSERT INTO messages VALUES (0, NULL, 2, 't', '2024/06/03 20:20:20', 'Hello this is Tom');
UPDATE users SET phonenumber = 447342780080 WHERE username = 't';

# Query 1
SELECT u.*, gm.group_id
FROM users u JOIn group_members gm ON u.username = gm.user;

# Query 2
SELECT u.*, COUNT(m.id) AS message_count
FROM users u JOIN messages m ON U.username = M.sender
WHERE m.group_id = 2
GROUP BY u.username
ORDER BY message_count DESC;

# Query 3
SELECT g.*, COUNT(c.id) AS private_chat_count
FROM chats AS c, msg_groups AS g
WHERE (g.id, c.user1, c.user2) in (SELECT g1.group_id, g1.user, g2.user
                             FROM group_members g1 JOIN group_members g2 ON g1.group_id = g2.group_id
                             WHERE g1.user <> g2.user)
GROUP BY g.id;

# Query 5
SELECT u.*
FROM users u JOIN group_members gm ON u.username = gm.user
WHERE u.username <> 'u0' and gm.group_id IN (SELECT group_id
                      FROM group_members
                      WHERE user = 'u0');
