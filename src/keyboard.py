from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


def menu():
    markup = InlineKeyboardMarkup(row_width=2)
    upload = InlineKeyboardButton(text="Upload file",
                                  callback_data="Upload file")
    download = InlineKeyboardButton(text="Download file",
                                    callback_data="Download file")
    markup.insert(upload)
    markup.insert(download)
    return markup
