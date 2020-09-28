import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from frames import *

set_dpi_awareness()

COLOR_PRIMARY = "#998888"
COLOR_LIGHT_BACKGROUND = "#fff"
COLOR_LIGHT_TEXT = "#eee"
COLOR_DARK_TEXT = "#8095a8"
COLOR_DARK_BACKGROUND = "#a9a9a9"


class ElevatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Elevator.TFrame", background=COLOR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOR_PRIMARY)
        style.configure(
            "ElevatorFloors.TLabel",
            foreground=COLOR_DARK_TEXT,
            font="Courier 32"
        )
        style.configure(
            "ElevatorAction.TLabel",
            foreground=COLOR_DARK_TEXT,
            font="Helvetica 12"
        )

        self["background"] = COLOR_PRIMARY
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.title("Elevator Simulator")
        self.geometry("1200x1100")
        self.columnconfigure(0, weight=1)

        self.floor = tk.StringVar(value="1")
        self.name = tk.StringVar()

        container = ttk.Frame(self)
        container.grid(pady=30)
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        elevator_floor_frame = ElevatorFloors(container, self, lambda: self.show_frame(MainMenu))
        elevator_floor_frame.grid(row=0, column=0, sticky="NSEW")
        main_menu_frame = MainMenu(
                                    container,
                                    self,
                                    lambda: self.show_frame(ElevatorFloors),
                                    lambda: self.show_frame(CreateUser),
                                    lambda: self.show_frame(ShowUsers),
                                    lambda: self.show_frame(GroupRide),
                                    lambda: self.show_frame(ShowElevator),
                                    lambda: self.show_frame(About)
                                  )
        main_menu_frame.grid(row=0, column=0, sticky="NSEW")
        create_user_frame = CreateUser(container, self, lambda: self.show_frame(MainMenu))
        create_user_frame.grid(row=0, column=0, sticky="NSEW")
        show_users_frame = ShowUsers(container, self, lambda: self.show_frame(MainMenu))
        show_users_frame.grid(row=0, column=0, sticky="NSEW")
        group_ride_frame = GroupRide(container, self, lambda: self.show_frame(MainMenu))
        group_ride_frame.grid(row=0, column=0, sticky="NSEW")
        show_elevator_frame = ShowElevator(container, self, lambda: self.show_frame(MainMenu))
        show_elevator_frame.grid(row=0, column=0, sticky="NSEW")
        about_frame = About(container, self, lambda: self.show_frame(MainMenu))
        about_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[ElevatorFloors] = elevator_floor_frame
        self.frames[MainMenu] = main_menu_frame
        self.frames[CreateUser] = create_user_frame
        self.frames[ShowUsers] = show_users_frame
        self.frames[GroupRide] = group_ride_frame
        self.frames[ShowElevator] = show_elevator_frame
        self.frames[About] = about_frame

        self.show_frame(MainMenu)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = ElevatorApp()
app.mainloop()


