# in-memory runtime data storage for the characters, elevator

from models import User, Elevator

users = []
elevator = Elevator(1, [])


def add_user(user: User):
    users.append(user)


def get_user(username):
    return [user for user in users if user.name == username][0]



