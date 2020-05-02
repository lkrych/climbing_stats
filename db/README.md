# Database stuff

The MVP uses Sqlite as the data store.

This file creates the database and loads the sql files from the `migrations` directory.

## Schema

### Database

1. Users
    1. primary_id - int
    2. username - string
    3. password_hash - string
    4. signup_date - string

2. Workout
    1. primary_id - int
    2. user_id - int (foreign key)
    2. date - int (unix timestamp)
    
3. Climbs
    1. primary_id - int
    2. user_id - int (foreign key)
    3. workout_id - int (foreign key)
    4. type - int (enum route or boulder)
    5. grade - int
    6. letter_grade - int (enum (a,b,c,d))

## Changing the schema

If you need to change the database schema, please create a sql file in the migrations file. 

## Interacting with the database

```bash
sqlite3 climbing_stats.db
```