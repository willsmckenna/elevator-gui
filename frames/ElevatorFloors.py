import tkinter as tk
from tkinter import ttk
from models import db

GREY_BACKGROUND = "#DCDCDC"


class ElevatorFloors(ttk.Frame):
    def __init__(self, parent, controller, show_frame):
        super().__init__(parent)

        self.controller = controller
        self.curr_floor = tk.StringVar(value="WAITING")
        self.dest_floor = tk.StringVar()
        self.curr_action = tk.StringVar(value=f"STOPPED")
        self.user = tk.StringVar()
        self._elevator_job = None

        # input to ride as a user
        prompt_container = tk.Frame(self)
        prompt_container.grid(row=0, column=0, columnspan=2, sticky="")
        prompt_container["background"] = GREY_BACKGROUND
        prompt_label = ttk.Label(prompt_container, text="RIDE AS: ", font=("Helvetica", 10))
        prompt_entry = ttk.Entry(prompt_container, width=5, textvariable=self.user, font=("Segoe UI", 15))
        prompt_label.grid(row=0, column=0, sticky="nsew")
        prompt_entry.grid(row=0, column=1, padx=(20,20), sticky="nsew")
        prompt_submit = tk.Button(
            prompt_container,
            text="GO",
            command=self.ride,
            cursor="hand2",
            borderwidth=4
        )
        prompt_submit.grid(row=0, column=2, sticky="nsew")
        # input for destination floor
        dest_floor_label = ttk.Label(self, text="Destination Floor: ")
        dest_floor_input = ttk.Entry(self, width=3, textvariable=self.dest_floor, font=("Segoe UI", 15))
        dest_floor_label.grid(row=4, column=0, sticky="e")
        dest_floor_input.grid(row=4, column=1, sticky="ew")
        # buttons
        button_container = ttk.Frame(self, padding=15)
        button_container.grid(row=5, column=0, columnspan=2, sticky="ew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        self.start_button = tk.Button(
            button_container,
            text="START",
            command=self.move,
            cursor="hand2",
            borderwidth=4

        )
        self.start_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.stop_button = tk.Button(
            button_container,
            text="STOP",
            command=self.stop,
            cursor="hand2",
            borderwidth=4
        )
        self.stop_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.back_button = tk.Button(
            button_container,
            text="-> Back",
            cursor="hand2",
            borderwidth=4,
            command=show_frame
        )
        self.back_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        # showing the state of the elevator (going up, down, etc)
        elevator_description = ttk.Label(
            self,
            textvariable=self.curr_action,
            style="ElevatorAction.TLabel",
        )
        elevator_description.grid(row=1, column=0, columnspan=2)

        # showing the curr floor in real time as it goes up/down
        floor_frame = ttk.Frame(self, height=150)
        floor_frame.grid(row=2, column=0, pady=(10, 0), padx=(30, 0), columnspan=2, sticky="nsew")
        floor_display = ttk.Label(
            floor_frame,
            textvariable=self.curr_floor,
            style="ElevatorFloors.TLabel"
        )
        floor_display.place(relx=0.5, rely=0.5, anchor="center")

        for child in self.winfo_children():
            child.grid_configure(padx=70, pady=50)

    def move(self):
        try:
            user = db.get_user(self.user.get())
        except IndexError:
            self.curr_action.set("User not found")
            return

        new_floor = 0
        current_floor = int(self.curr_floor.get().split(" ")[1])
        if current_floor == int(self.dest_floor.get()):
            self.curr_action.set(f"{user.name.upper()} IS STOPPED")
        else:
            if current_floor > int(self.dest_floor.get()):
                self.curr_action.set(f"{user.name.upper()} IS GOING DOWN")
                new_floor = current_floor - 1
            elif current_floor < int(self.dest_floor.get()):
                self.curr_action.set(f"{user.name.upper()} IS GOING UP")
                new_floor = current_floor + 1

            self.curr_floor.set(f"FLOOR {new_floor}")
            user.wait_floor = new_floor
            self._elevator_job = self.after(1000, self.move)

    def stop(self):
        if self._elevator_job:
            self.after_cancel(self._elevator_job)
            self.curr_action.set("STOPPED")
            self._elevator_job = None

    def ride(self):
        self.curr_action.set("STOPPED")
        try:
            user = db.get_user(self.user.get())
        except IndexError:
            self.curr_action.set("User not found")
            return
        self.curr_floor.set(f"FLOOR {user.wait_floor}")
        self.dest_floor.set(user.dest_floor)