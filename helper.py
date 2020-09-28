def change_message(elevator, controller, num_floors, user):
    if num_floors != 0:
        num_floors -= 1
        message = elevator.state.move_elevator(elevator, user)
        controller.moving_message.set(message)
        controller.after(1000, lambda: change_message(elevator, controller, num_floors, user))
