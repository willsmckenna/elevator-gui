from models import User
from typing import List
from helper import change_message

# Elevator class used for multiple user rides

class Elevator:
    def __init__(self, curr_floor, users: List[User]):
        self.curr_floor = curr_floor
        self.users = users

    def __repr__(self):
        return f"Elevator is at floor {self.curr_floor}---{len(self.users)} passengers\n"


    def send_arrival_msg(self, user: User, dest_floor):
        print(f"Arrived at floor {dest_floor} for {user.name}")

    def pick_up(self, user: User, controller):
        self.users.append(user)
        controller.message.set(f"Picked up {user.name}")

    def drop_off(self, user: User, controller):
        self.users.remove(user)
        controller.message.set(f"Dropped off {user.name}")
        # also change the user's current wait floor to the floor they just arrived to
        user.wait_floor = user.dest_floor

