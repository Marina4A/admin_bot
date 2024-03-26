import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config import config_get
from src.dialogs import register_user_dialog
from src.handlers.services import start_handler
from aiogram.filters.command import CommandStart


async def main():
    config = config_get()
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.bot.token, default=default)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(start_handler, CommandStart())
    register_user_dialog(dp=dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
