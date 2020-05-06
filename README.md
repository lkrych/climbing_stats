# 🧗‍♀️climbing_stats 🧗

A service for recording climbing workouts.

Supports both bouldering workouts or sport climbing workouts.

### Table of Contents
* [Quickstart](#quickstart)
* [Application Organization](#application-organization)
* [API Spec](#api-spec)

### Quickstart


| Command       | Description   |
| ------------- |-------------|
| Local Development | ```make backend-dev```| 
| Docker Development | ```make docker-dev``` |
| Frontend Devleopment | ``` make frontend-dev ``` |
| Run Tests | ``` make test``` |   
| Initialize and Seed Database | ``` make init-db ``` |   

### Development work

Setup dependencies (built in to local development script)

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

### Application Organization

Climbing Stats is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [React](https://reactjs.org/) application.

```
climbing_stats/
├── climbing_stats_backend/       <--- Flask backend directory
      ├── __init__.py                 <--- Flask entrypoint, initializes connection with database and registers routes
      ├── routes.py                   <--- Defines routes for service
      ├── config.py                   <--- Application configuration
      ├── helpers/                    <--- Directory of helpful functions
          ├── auth_helpers.py             <--- Definition of JWT auth decorator
          ├── factory_helpers.py          <--- Initalizes DB and Bcrypt 
          ├── model_helpers.py            <--- Helper Methods for the Models (users, workouts, climbs)
          ├── seeds.py                    <--- Definition of Flask utility methods for resetting and seeding the DB
          ├── util_helpers.py             <--- General Helper Methods 
      ├── models/                     <--- Directory of ORM Classes
          ├── climb.py                    
          ├── user.py                     
          ├── workout.py                  
├── db/                           <--- Database-related directory
      ├── migrations/                 <--- SQL migrations directory
      ├── init_db.py/                 <--- Initial Database Setup
      ├── climbing_stats.db           <--- Local Sqlite3 copy of DB
├── frontend/                     <--- React Frontend
      ├── .env                        <--- Environment Variable Declaration
      ├── index.html                  <--- HTML Entrypoint, where our React code is mounteds
      ├── package.json                <--- Frontend Script definition, Parcel Setup
      ├── src/                        <--- React Code Directory
          ├── App.js                      <--- Definition of application 
          ├── Index.js                    <--- React Entrypoint
          ├── components/                 <--- Directory of all React components
          ├── util/                       <--- Directory of all Helper functions
├── tests/                        <--- Python Backend Tests
      ├── conftest.py                 <--- Test Database Initialization
      ├── functional/                 <--- Functional API test direcotry
      ├── helpers/                    <--- Useful Test helpers
      ├── unit/                       <--- Unit Test directory
├── Dockerfile                    <--- Ubuntu-based Docker Image
├── Makefile                      <--- Collection of useful scripts
├── requirements.txt              <--- Python dependencies
├── todo.md                       <--- File to keep track of what to do
```
### API Spec

The Climbing Stats API has 14 endpoints. All of the endpoints besides the index, login, and user creation are protected by JWT.

* `/` - GET - healthcheck
* `/login` - POST - Fetch a JWT with proper user credentials

* `/user/<user_id>` - GET - Fetch a user
* `/users` - POST - Create a User
* `/user/<user_id>` - PUT/PATCH - Update a user
* `/user/<user_id>` - DELETE - Delete a user

* `/user/<user_id/workout/<workout_id>` - GET - Fetch a workout
* `/user/<user_id/workouts` - POST - Create a workout for a user
* `/user/<user_id/workout/<workout_id>` - PUT/PATCH - Update a workout
* `/user/<user_id/workout/<workout_id>` - DELETE - Delete a workout

* `/user/<user_id>/climb/<climb_id>` - GET - Fetch a climb
* `/user/<user_id>/climbs` - POST - Create a climb for a user
* `/user/<user_id>/climb/<climb_id>` - PUT/PATCH - Update a climb
* `/user/<user_id>/climb/<climb_id>` - DELETE - Delete a climb

### JSON definition of workout

Workout should be created with a JSON-serialized object that looks like the object below

```json
{
  "date": 1577865600,
  "boulders": [5, 6],
  "routes": ["12d", "11a", "12c", "12c", "11c"]
}
```