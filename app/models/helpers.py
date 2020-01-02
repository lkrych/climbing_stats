from app import db, bcrypt
from app.models.user import Users
from app.models.workout import Workouts

### USER HELPER METHODS ###########
def get_user(id):
    return db.session.query(Users).get(id)

def create_user(req_json):
    new_user = Users(
        username=req_json['username'],
        email=req_json['email'],
        password_hash=bcrypt.generate_password_hash(req_json['password']).decode('utf-8')
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

### WORKOUT HELPER METHODS ########