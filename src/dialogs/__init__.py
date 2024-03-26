from aiogram import Dispatcher
from aiogram_dialog import Dialog, setup_dialogs

from src.dialogs.main_dialogs import main_dialog


def register_user_dialog(dp: Dispatcher) -> None:
    dialogs = Dialog(main_dialog())
    dp.include_routers(dialogs)
    setup_dialogs(dp)
