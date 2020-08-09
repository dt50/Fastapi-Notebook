-- name: create-user-note^
INSERT INTO Notes (
    id_users,
    title,
    description
) VALUES (
    :id_user,
    :title,
    :description
)
RETURNING id, title, description;

--name: get-all-user-notes
SELECT Notes.id,
    Notes.title,
    Notes.description
FROM Notes
INNER JOIN Users
    ON Notes.id_users=Users.id
WHERE
    Users.login = :login
    AND
    Users.password = crypt(
    :password,
    Users.password
);

--name: get-user-note^
SELECT Notes.title,
    Notes.description
FROM Notes
INNER JOIN Users
    ON Notes.id_users=Users.id
WHERE
    Users.login = :login
    AND
    Users.password = crypt(
    :password,
    Users.password)
    AND
    Notes.id = :id;

--name: update-user-note^
UPDATE Notes
SET
    title = :title,
    description = :description
WHERE id_users = (
    SELECT id
    FROM Users
    WHERE login = :login
    AND
    password = crypt(
        :password,
        password
    )
    AND
    Notes.id = :id
)
RETURNING id, title, description;

--name: delete-user-note^
DELETE FROM Notes
WHERE
    id = :id
    AND
    id_users = (
        SELECT id
        FROM Users
        WHERE login = :login
        AND
        password = crypt(
            :password,
            password
        )
);