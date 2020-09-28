import tkinter as tk
from tkinter import ttk
from models import db, elevator as el

GREY_BACKGROUND = "#DCDCDC"


class GroupRide(ttk.Frame):
    def __init__(self, parent, controller, show_frame):
        super().__init__(parent)

        self.user = tk.StringVar()
        self.message = tk.StringVar(value="Elevator is stopped")
        self.floor = tk.StringVar()
        self.floor.set(f"FLOOR {el.curr_floor}")
        self.curr_floor = tk.StringVar()
        self._elevator_job = None
        self.user_pickup_queue = []
        self.user_dropoff_queue = []

        prompt_container = tk.Frame(self)
        prompt_container.grid(row=0, column=0, columnspan=2, sticky="")
        prompt_container["background"] = GREY_BACKGROUND
        prompt_label = ttk.Label(prompt_container, text="INPUT USER(S): ", font=("Helvetica", 10))
        prompt_entry = ttk.Entry(prompt_container, width=5, textvariable=self.user, font=("Segoe UI", 15))
        prompt_label.grid(row=0, column=0, sticky="nsew")
        prompt_entry.grid(row=0, column=1, padx=(20, 20), sticky="nsew")
        prompt_submit = tk.Button(
            prompt_container,
            text="ADD",
            command=self.add_user_to_queue,
            cursor="hand2",
            borderwidth=4
        )
        prompt_submit.grid(row=0, column=2, sticky="nsew")

        # buttons
        button_container = ttk.Frame(self, padding=15)
        button_container.grid(row=4, column=0, columnspan=2, sticky="ew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        self.pickup_button = tk.Button(
            button_container,
            text="PICKUP",
            command=self.move_pick_up,
            cursor="hand2",
            borderwidth=4
        )
        self.pickup_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.dropoff_button = tk.Button(
            button_container,
            text="DROPOFF",
            command=self.move_drop_off,
            cursor="hand2",
            borderwidth=4
        )
        self.dropoff_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.back_button = tk.Button(
            button_container,
            text="-> Back",
            cursor="hand2",
            borderwidth=4,
            command=show_frame
        )
        self.back_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # showing the curr floor in real time as it goes up/down
        floor_frame = ttk.Frame(self, height=150)
        floor_frame.grid(row=2, column=0, pady=(10, 0), padx=(30, 0), columnspan=2, sticky="nsew")
        floor_display = ttk.Label(
            floor_frame,
            textvariable=self.floor,
            style="ElevatorFloors.TLabel"
        )
        floor_display.place(relx=0.5, rely=0.5, anchor="center")

        message_frame = ttk.Frame(self, height=100)
        message_frame.grid(row=3, column=0, pady=(10, 0), padx=(30, 0), columnspan=2, sticky="nsew")
        message_display = ttk.Label(
            message_frame,
            textvariable=self.message,
            style="ElevatorAction.TLabel"
        )
        message_display.place(relx=0.5, rely=0.5, anchor="center")

        for child in self.winfo_children():
            child.grid_configure(padx=60, pady=50)

    def add_user_to_queue(self):
        try:
            user = db.get_user(self.user.get())
        except IndexError:
            self.message.set("User not found")

        self.user_pickup_queue.append(user)
        self.user.set("")

    def move_drop_off(self):
        user = self.user_dropoff_queue[0]
        user_floor = user.dest_floor
        if user.dest_floor > el.curr_floor:
            message = f"Moving up to drop off {user.name}"
        else:
            message = f"Moving down to drop off {user.name}"
        self.move(user, user_floor, el.drop_off, message)
        self.user_dropoff_queue.pop(0)

    def move_pick_up(self):
        user = self.user_pickup_queue[0]
        user_floor = user.wait_floor
        if user.wait_floor < el.curr_floor:
            message = f"Moving down to pick up {user.name}"
        else:
            message = f"Moving up to pick up {user.name}"
        self.move(user, user_floor, el.pick_up, message)
        self.user_pickup_queue.pop(0)
        self.user_dropoff_queue.append(user)

    def move(self, user, user_floor, el_action, message):
        if el.curr_floor == user_floor:
            el_action(user, self)
        else:
            if el.curr_floor < user_floor:
                self.message.set(message)
                el.curr_floor += 1
            elif el.curr_floor > user_floor:
                self.message.set(message)
                el.curr_floor -= 1

            self.floor.set(f"FLOOR {el.curr_floor}")
            self.after(1000, lambda: self.move(user, user_floor, el_action, message))
