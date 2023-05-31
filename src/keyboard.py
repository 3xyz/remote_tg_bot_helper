from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def menu():
    markup = InlineKeyboardMarkup(row_width=2)
    upload = InlineKeyboardButton(text="Upload file", callback_data="Upload file")
    download = InlineKeyboardButton(text="Download file", callback_data="Download file")
    cd = InlineKeyboardButton(text="cd", callback_data="cd")
    markup.insert(upload)
    markup.insert(download)
    markup.insert(cd)
    return markup

