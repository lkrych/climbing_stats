# 🧗‍♀️climbing_stats 🧗

A service for recording climbing workouts.

You can enter bouldering workouts or Sport Climbing workouts.

And view your progress across time with the summary command.

### Quickstart


| Command       | Description   |
| ------------- |-------------|
| Local Development | ```make start-dev```| 
| Docker Development | ```make docker-dev``` |
| Run Tests | ``` make run-tests``` |   
| Initialize and Seed Database | ``` make init-db ``` |   

### Development work

Setup dependencies

```bash
python -m venv climbing_stats_venv
source climbing_stats_venv/bin/activate
pip install -r requirements.txt
```

### Resetting and Seeding Database

```bash
flask reset-db 
flask seed-db
```

More [database information](db/README.md)

### API Examples

# Unprotected Routes

These routes do not require a JWT

To get a JWT

# /login

```bash
curl -d '{"username":"blah", "password":"blahblah"}' -H "Content-Type: application/json" -X POST http://localhost:5000/login
{
  "access_token": "<ACCESS TOKEN GOES HERE>"
}
```

# /users create

```bash
curl -d '{"username":"blah", "email":"blahblah@blah.com", "password":"blahblah"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users
```
# Protected Routes

All protected routes need an Authorization Header.

```bash
curl -H "Authorization: JWT <ACCESS TOKEN GOES HERE>" http://localhost:5000/user/1/workout/2
```

# /users read

```bash
    curl localhost:5000/user/1
```
# /workout create

The payload can have boulder, routes or both.

```bash
curl -d '{"date": 1577865600,"boulder": [5, 6], "routes": ["12d", "11a", "12c", "12c", "11c"]}' -H "Content-Type: application/json"
-H "Authorization: JWT <ACCESS TOKEN GOES HERE>" -X POST http://localhost:5000/user/blah/workouts
```

