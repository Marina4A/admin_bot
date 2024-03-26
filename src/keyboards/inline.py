from aiogram import types


def get_keyboard():
    # builder = InlineKeyboardBuilder()
    buttons = [[types.InlineKeyboardButton(text="Menu", callback_data="menu")],
               [types.InlineKeyboardButton(text='Help', callback_data='help')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
    # return buttons