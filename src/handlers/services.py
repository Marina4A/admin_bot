from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

from src.filters.KeyboardsFilter import KeyboardsFilter
from src.filters.admin_filter import AdminIdFilter

router = Router()
router.message.filter(AdminIdFilter(admin_id='797910499'))


@router.message(Command(commands="start"))
async def start_handler(massage: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми на меня",
        callback_data="+"
    ))
    await massage.answer("Алёшка меня обижает", reply_markup=builder.as_markup())


@router.callback_query(KeyboardsFilter(data="+"))
async def send_msg(callback: typs.CallbackQuery):
    await callback.message.answer("Алёша, не обижай Марину!")


@router.message(Command("help"))
async def message_handler(massage: Message):
    await massage.answer(f"Твой ID: {massage.from_user.id}")

# @router.message(Command("admins"))
# async def message_handler(massage: Message):
#     await massage.answer(f"Твой ID: {massage.from_user.id}")
