CREATE TABLE IF NOT EXISTS climbs (
    id integer PRIMARY KEY,
    user_id integer NOT NULL,
    workout_id integer NOT NULL,
    type integer NOT NULL,          -- 0, 1 = boulder, routes
    grade integer NOT NULL,
    letter_grade integer,           -- 0, 1, 2, 3 = a, b, c, d
    FOREIGN KEY (user_id) REFERENCES users (id)
    FOREIGN KEY (workout_id) REFERENCES workouts (id)
);