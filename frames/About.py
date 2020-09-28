import tkinter as tk
from tkinter import ttk

MESSAGE = """
VERSION 1.1

Made with python 3.8 
and tkinter GUI library

Use the solo elevator options to
change the destination floor for 
a user. In group ride, the elevator 
picks up users in the order they 
were created and drops them off 
in the order they were picked up, 
i.e a first in first out stack.
If you forget the name of a user 
when doing group ride you can 
always go to the show users page 
to see who is in the database. 
"""


class About(ttk.Frame):
    def __init__(self, parent, controller, show_frame):
        super().__init__(parent)

        message_container = tk.Frame(self)
        message_container.grid(row=0, column=0, pady=(20, 60), padx=(100, 0), columnspan=2, sticky="nsew")
        main_message_label = ttk.Label(message_container, text=MESSAGE, font=("Segoe UI bold", 10))

        main_message_label.grid(row=0, column=0, sticky="nsew")

        button_container = ttk.Frame(self)
        button_container.grid(row=1, column=0, sticky="NSEW")
        back_button = tk.Button(
            button_container,
            text="-> Back",
            cursor="hand2",
            borderwidth=4,
            command=show_frame
        )
        back_button.grid(row=0, column=1, padx=(10, 20), pady=(20, 20), sticky="nsew")