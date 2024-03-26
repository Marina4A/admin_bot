from typing import Any

from aiogram import types
from aiogram.filters import BaseFilter


class KeyboardsFilter(BaseFilter):
    def __init__(self, data: Any):
        self.data = data

    async def __call__(self, callback: types.CallbackQuery) -> bool:
        if callback.data == self.data:
            return True
        return False
