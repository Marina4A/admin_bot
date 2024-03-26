from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from src.states import UserStates


async def start_handler(message: Message, dialog_manager: DialogManager) -> None:
    # name = message.from_user.first_name
    await message.delete()
    await dialog_manager.start(UserStates.main, mode=StartMode.RESET_STACK)

