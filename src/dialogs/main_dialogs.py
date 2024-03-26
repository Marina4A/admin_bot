from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from src.states import UserStates


def main_dialog() -> Window:
    main_window = Window(
        Const(f"Welcome back!"),  # just a constant text
        Button(Const("Menu"), id="menu"),  # button with text and id
        Button(Const("Help"), id="help"),  # button with text and id
        state=UserStates.main,  # state is used to identify window between dialogs
    )
    return main_window
