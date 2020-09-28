import tkinter as tk
from tkinter import ttk
from models import User, db


class ShowUsers(ttk.Frame):
    def __init__(self, parent, controller, show_frame):
        super().__init__(parent)

        button_container = ttk.Frame(self)
        button_container.grid(row=0, column=0, columnspan=2, sticky="nsew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        create_user_button = tk.Button(
            button_container,
            text="Show All Users",
            cursor="hand2",
            borderwidth=4,
            command=self.show_users
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


    def show_users(self):
        container = tk.Frame(self)
        container.grid(row=1, column=0, sticky="nsew")
        for i, user in enumerate(db.users):
            username_label = ttk.Label(
                container,
                text=f" {user.name}--",
                font=("Segoe UI", 12)
            )
            username_label.grid(row=i, column=0, sticky="nsew")
            curr_floor_label = ttk.Label(
                container,
                text=f"Curr Floor: {user.wait_floor}--",
                font=("Segoe UI", 12)
            )
            curr_floor_label.grid(row=i, column=1, sticky="nsew")
            dest_floor_label = ttk.Label(
                container,
                text=f"Dest Floor: {user.dest_floor}",
                font=("Segoe UI", 12)
            )
            dest_floor_label.grid(row=i, column=2, sticky="nsew")








