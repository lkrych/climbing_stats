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

# /workout create


### Bouldering workout

Valid boulders are 0 - 16

```json
{
    "date": 1577865600,
    "boulder": [1,1,2,5,3,2,1,5,4]
}
```

### Sport climbing workout

Valid routes are 0 - 15 with letter grade

```json
{
    "date": 1577865600, 
    "routes": ["10a", "11c", "12a", "11c", "11c", "10a", "10a", "11c"]
}
```

### or both

```json
{
    "date": 1577865600,
    "boulder": [5, 6],
    "routes": ["12d", "11a", "12c", "12c", "11c"]
}

```
