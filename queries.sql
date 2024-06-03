INSERT INTO users VALUES ('t', 'Tom', 'Kane', 'tk', 44796268462);
INSERT INTO group_members VALUES (1, 't');
INSERT INTO messages VALUES (0, NULL, 1, 't', '2024/06/03 20:20:20', 'Hello this is Tom');
UPDATE users SET phonenumber = 447342780080 WHERE username = 't';

SELECT u.*, g.*
FROM users u JOIN group_members gm ON u.username = gm.user JOIN msg_groups g ON gm.group_id = g.id;

SELECT u.*, COUNT(m.id) AS message_count
FROM users u JOIN messages m ON u.username = m.sender
WHERE m.group_id = 1
GROUP BY u.username
ORDER BY message_count DESC;

SELECT g.*, COUNT(c.id) AS private_chat_count
FROM msg_groups g
JOIN group_members gm ON g.id = gm.group_id
JOIN chats c ON (gm.user = c.user1 OR gm.user = c.user2)
GROUP BY g.id;

SELECT u.*
FROM users u
LEFT JOIN group_members gm ON u.username = gm.user
LEFT JOIN chats c1 ON u.username = c1.user1
LEFT JOIN chats c2 ON u.username = c1.user2
WHERE gm.group_id IS NOT NULL OR c1.user2 IS NOT NULL OR c2.user1 IS NOT NULL
GROUP BY u.username;
