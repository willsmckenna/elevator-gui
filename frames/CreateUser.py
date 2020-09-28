import tkinter as tk
from tkinter import ttk
from models import User, db


class CreateUser(ttk.Frame):
    def __init__(self, parent, controller, show_frame):
        super().__init__(parent)

        self.controller = controller
        self.username = tk.StringVar()
        self.curr_floor = tk.StringVar()
        self.dest_floor = tk.StringVar()

        header_label = ttk.Label(self, text="CREATE NEW USER", style="ElevatorAction.TLabel")
        header_label.grid(row=0, column=0, sticky="nsew")

        username_label = ttk.Label(self, text="Username: ", font=("Segoe UI", 12))
        username_label.grid(row=1, column=0, padx=(10, 0), pady=(100,10), sticky="nsew")
        username_entry = ttk.Entry(self, width=10, textvariable=self.username, font=("Segoe UI", 12))
        username_entry.grid(row=1, column=1, pady=(100,10), padx=(0, 20), sticky="e")

        curr_floor_label = ttk.Label(self, text="Current Floor: ", font=("Segoe UI", 12))
        curr_floor_label.grid(row=2, column=0, padx=(10, 0), pady=(10,10), sticky="nsew")
        curr_floor_entry = ttk.Entry(self, width=10, textvariable=self.curr_floor, font=("Segoe UI", 12))
        curr_floor_entry.grid(row=2, column=1, padx=(10, 20), pady=(10,10), sticky="nsew")

        dest_floor_label = ttk.Label(self, text="Destination Floor: ", font=("Segoe UI", 12))
        dest_floor_label.grid(row=3, column=0, padx=(10, 0), pady=(10,10), sticky="nsew")
        dest_floor_entry = ttk.Entry(self, width=10, textvariable=self.dest_floor, font=("Segoe UI", 12))
        dest_floor_entry.grid(row=3, column=1,padx=(10, 20), pady=(10,10), sticky="nsew")

        button_container = ttk.Frame(self, padding=15)
        button_container.grid(row=4, column=0, columnspan=2, sticky="ew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        self.submit_button = tk.Button(
            button_container,
            text="Add",
            command=self.add_user,
            cursor="hand2",
            borderwidth=4
        )
        self.submit_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.back_button = tk.Button(
            button_container,
            text="-> Back",
            command=show_frame,
            cursor="hand2",
            borderwidth=4

        )
        self.back_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=20)

    def add_user(self):
        new_user = User(1, self.username.get(), int(self.curr_floor.get()), int(self.dest_floor.get()))
        db.add_user(new_user)
        self.username.set("")
        self.curr_floor.set("")
        self.dest_floor.set("")

