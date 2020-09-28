import tkinter as tk
from tkinter import ttk
from frames import ElevatorFloors

MESSAGE = """
    ELEVATOR RIDE
    
Welcome to the elevator 
app, where you can create 
users to ride an elevator 
in a 40 story building. 
Solo ride as one user or 
have multiple users ride 
the elevator at one time.
"""


class MainMenu(ttk.Frame):
    def __init__(self, parent, controller, show_elevator, show_create_user, show_users, group_ride, show_el_contents, show_about):
        super().__init__(parent)

        message_container = tk.Frame(self)
        message_container.grid(row=0, column=0, pady=(20, 60), padx=(100, 0), columnspan=2, sticky="nsew")
        main_message_label = ttk.Label(message_container, text=MESSAGE, font=("Segoe UI bold", 10))

        main_message_label.grid(row=0, column=0, sticky="nsew")

        button_container = ttk.Frame(self)
        button_container.grid(row=1, column=0, columnspan=3, sticky="nsew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        create_user_button = tk.Button(
            button_container,
            text="Create User",
            cursor="hand2",
            borderwidth=4,
            command=show_create_user
        )
        create_user_button.grid(row=0, column=0, padx=(50,0), sticky="nsew")
        solo_ride_button = tk.Button(
            button_container,
            text="Ride Solo",
            cursor="hand2",
            borderwidth=4,
            command=show_elevator
        )
        solo_ride_button.grid(row=0, column=1, sticky="nsew")
        show_users_button = tk.Button(
          button_container,
          text="Show Users",
          cursor="hand2",
          borderwidth=4,
          command=show_users
        )
        show_users_button.grid(row=0, column=2, sticky="nsew")
        show_el_button = tk.Button(
            button_container,
            text="Elevator",
            cursor="hand2",
            borderwidth=4,
            command=show_el_contents
        )
        show_el_button.grid(row=1, column=0, padx=(50,0), sticky="nsew")
        group_ride_button = tk.Button(
            button_container,
            text="Group Ride",
            cursor="hand2",
            borderwidth=4,
            command=group_ride
        )
        group_ride_button.grid(row=1, column=1, sticky="nsew")
        about_button = tk.Button(
            button_container,
            text="About",
            cursor="hand2",
            borderwidth=4,
            command=show_about
        )
        about_button.grid(row=1, column=2, sticky="nsew")

