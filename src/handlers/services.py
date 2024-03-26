from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

from src.filters.keyboards_filter import KeyboardsFilter
from src.filters.admin_filter import AdminIdFilter
from src.keyboards.inline import get_keyboard

router = Router()
router.message.filter(AdminIdFilter(admin_id='797910499'))


@router.message(Command(commands="start"))
async def start_handler(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Welcome back, {name}!", reply_markup=get_keyboard())


@router.callback_query(KeyboardsFilter(data="menu"))
async def send_msg(callback: types.CallbackQuery):
    await callback.message.answer("Алёша, не обижай Марину!")


@router.message(Command("help"))
async def message_handler(message: Message):
    await message.answer(f"Твой ID: {message.from_user.id}")

# @router.message(Command("admins"))
# async def message_handler(massage: Message):
#     await massage.answer(f"Твой ID: {massage.from_user.id}")
