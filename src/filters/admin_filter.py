from aiogram.types import Message
from aiogram.filters import BaseFilter


class AdminIdFilter(BaseFilter):
    def __init__(self, admin_id: list | str | tuple):
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        id_user: str = str(message.from_user.id)
        if isinstance(self.admin_id, str):
            if id_user == self.admin_id:
                return True
        elif isinstance(self.admin_id, (list, tuple)):
            if id_user in self.admin_id:
                return True
        return False
