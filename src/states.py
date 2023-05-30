from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup


class Get(StatesGroup):
    path = State()


class Download(StatesGroup):
    file = State()


class Upload(StatesGroup):
    file = State()
