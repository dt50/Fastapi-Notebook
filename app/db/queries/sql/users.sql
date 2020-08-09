-- name: create-user^
INSERT INTO Users
(login, password)
VALUES (
    :login,
    crypt(
        :password,
        gen_salt('bf', 8)
    )
)
RETURNING login, id;

--name: get-user-id^
SELECT login, id
FROM Users
WHERE
    login = :login
    AND
    password = crypt(
        :password,
        password
    );