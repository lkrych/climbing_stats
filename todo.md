# Todo list

## MVP 

### 4/3-4/5 Hackathon

* [ ] Data Presentation: Frontend
    * [ ] Histogram
    * [ ] Summary Stats
    * [ ] Time period, last week, last month, last year
    * [ ] Mobile-first design 
    * [ ] User stories/features:
        * [x] Sign up for service
        * [x] Log in to/log out of service
        * [ ] Log a workout (consisting of 1+ climbs) -> form
        * [ ] On login, see composite of climbing stats (last week, last month, last year)

* [x] Backend
    * [x] use a production-grade server in docker

* [ ] Containerization and prepare for deployment
    * [X] Build Docker file
    * [ ] Terraform plan resources
* [ ] CI/CD
    * [x] Backend Testing
    * [ ] Frontend Testing
    * [x] CI with GitHub


## Nice to have (future hackathon)
* [ ] Git Hook for push?
* [ ] Clean up Readme, combine all of 'em
* [ ] E-mail confirmation for signup to guard user creation
* [ ] Strava link/push --> dependent on Data Presentation
* [ ] Rate-Limiting
* [ ] Followers
* [ ] Kudos
* [ ] Logging of time to resolve endpoint
* [ ] User can see specific workouts/workout stats/notes
* [ ] User can log what gym they worked out at
* [ ] Public domain


1/2/2020
* [x] Read/Create Endpoints
    1. [x] User
    2. [x] Workout
    3. [x] Climb
* [x] Return climbs with workout
* [x] Add Update Endpoints
    1. [x] User
    2. [x] Workout
    3. [x] Climb
* [x] Add Delete Endpoints
    1. [x] User
    2. [x] Workout
    3. [x] Climb
1/3/2020
* [x] Authentication of certain routes
    1. [x] JWT
    2. [x] Login
    3. [ ] Only allow access to resources you own
* [ ] Testing
    1. [ ] Unit tests
    2. [ ] Functional Tests
        * [ ] Auth
        * [ ] User
        * [ ] Workouts
        * [ ] Climbs


