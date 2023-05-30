from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData


def menu():
    markup = InlineKeyboardMarkup(row_width=2)
    upload = InlineKeyboardButton(text="Upload file", callback_data="Upload file")
    download = InlineKeyboardButton(text="Download file", callback_data="Download file")
    cd = InlineKeyboardButton(text="cd", callback_data="cd")
    general_commands = InlineKeyboardButton(text="General", callback_data="General")
    markup.insert(upload)
    markup.insert(download)
    markup.insert(cd)
    markup.insert(general_commands)
    return markup


def general():
    markup = InlineKeyboardMarkup(row_width=2)
    cpu = InlineKeyboardButton(text="CPU", callback_data="CPU")
    ram = InlineKeyboardButton(text="RAM", callback_data="RAM")
    disc_space = InlineKeyboardButton(text="Disc Space", callback_data="Disc Space")
    temp = InlineKeyboardButton(text="Temp", callback_data="Temp")
    back = InlineKeyboardButton(text="back", callback_data="menu")
    markup.insert(cpu)
    markup.insert(ram)
    markup.insert(disc_space)
    markup.insert(temp)
    markup.insert(back)
    return markup
