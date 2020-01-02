# 🧗‍♀️climbing_stats 🧗

A service for recording climbing workouts.

You can enter bouldering workouts or Sport Climbing workouts.

And view your progress across time with the summary command.

### Start server

```bash
make start
```

### Development work

Setup dependencies

```bash
python -m venv climbing_stats_venv
source climbing_stats_venv/bin/activate
pip install -r requirements.txt
```

# /users read

```bash
    curl localhost:5000/user/1
```

# /users create

```bash
curl -d '{"username":"blah", "email":"blahblah@blah.com", "password":"blahblah"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users
```

# /workout create

The payload can have boulder, routes or both.

```bash
curl -d '{"date": 1577865600,"boulder": [5, 6], "routes": ["12d", "11a", "12c", "12c", "11c"]}' -H "Content-Type: application/json" -X POST http://localhost:5000/user/blah/workouts
```

