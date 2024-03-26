from environs import Env
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Bot:
    token: str


@dataclass(frozen=True)
class Config:
    bot: Bot


def config_get(path=os.path.join(os.getcwd(), ".env")):
    env = Env()
    env.read_env(path=path)
    return Config(bot=Bot(token=env.str("BOT_TOKEN")))
