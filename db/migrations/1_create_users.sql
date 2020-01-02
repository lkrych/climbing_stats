CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    username text NOT NULL,
    email text NOT NULL,
    password_hash text NOT NULL,
    signup_date text
);