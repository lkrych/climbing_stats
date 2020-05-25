-- projects table
CREATE TABLE IF NOT EXISTS workouts (
    id integer PRIMARY KEY,
    user_id integer NOT NULL,
    date text NOT NULL,
    notes text,
    FOREIGN KEY (user_id) REFERENCES users (id)
);