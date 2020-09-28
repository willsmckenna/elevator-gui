import tkinter as tk
from tkinter import ttk
from models import db

GREY_BACKGROUND = "#DCDCDC"

class ShowElevator(ttk.Frame):
    def __init__(self, parent, controller, show_frame):
        super().__init__(parent)

        button_container = ttk.Frame(self)
        button_container.grid(row=0, column=0, columnspan=2, sticky="nsew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        create_user_button = tk.Button(
            button_container,
            text="Show Elevator Info",
            cursor="hand2",
            borderwidth=4,
            command=self.show_elevator_info
        )
        create_user_button.grid(row=0, column=0, padx=(150,20), pady=(20,20), sticky="nsew")
        back_button = tk.Button(
            button_container,
            text="-> Back",
            cursor="hand2",
            borderwidth=4,
            command=show_frame
        )
        back_button.grid(row=0, column=1, padx=(10, 20), pady=(20, 20), sticky="nsew")

    def show_elevator_info(self):
        container = tk.Frame(self)
        container["background"] = GREY_BACKGROUND
        container.grid(row=1, column=0, sticky="nsew")
        elevator_description = ttk.Label(
                container,
                text=f" {db.elevator.__repr__()}",
                font=("Segoe UI", 12)
            )
        elevator_description.grid(row=0, column=0, sticky="NSEW")
        users_in_elevator = db.elevator.users
        for i, user in enumerate(users_in_elevator):
            user_label = tk.Label(
                container,
                text=f"Name: {user.name}---Dest floor: {user.dest_floor}",
                font=("Segoe UI", 12),
                background=GREY_BACKGROUND
            )
            user_label.grid(row=i+2, column=0, sticky="NSEW")
