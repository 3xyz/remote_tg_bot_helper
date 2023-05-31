from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types.input_file import InputFile
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from src import keyboard
from src import misc
from src.config import ADMIN_IDS
from src.loader import bot
from src.loader import dp
from src.states import Get, Download, Upload
from src.misc import Dir


@dp.message_handler(CommandStart(), state="*")
async def menu_start(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_IDS:
        await state.finish()
        await menu_mes(message.from_user.id)

    
@dp.callback_query_handler(text="menu")
async def menu(call: CallbackQuery):
    if call.from_user.id in ADMIN_IDS:
        kb = keyboard.menu()
        pwd = Dir[call.from_user.id]
        await call.message.edit_text((f"`{pwd}`\n➖➖➖➖➖➖➖➖➖➖\n"), reply_markup=kb, parse_mode="Markdown")
        await call.answer(show_alert=False)


async def menu_mes(user_id, mes=''):
    kb = keyboard.menu()
    pwd = Dir[user_id]
    await bot.send_message(user_id, f"`{pwd}`\n➖➖➖➖➖➖➖➖➖➖\n{mes}", reply_markup=kb, parse_mode="Markdown")


@dp.callback_query_handler(text="cd")
async def execute_command(call: CallbackQuery):
    if call.from_user.id in ADMIN_IDS:
        await call.message.edit_text("Write directory:")
        await Get.path.set()

    
@dp.message_handler(state=Get.path)
async def try_change_path(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_IDS:
        await state.finish()
        path = message.text
        status = misc.change_dir(path, message.from_user.id)
        if status:
            await menu_mes(message.from_user.id)
        else:
            await menu_mes(message.from_user.id, 'No such directory')


@dp.callback_query_handler(text="Download file") 
async def download_file(call: CallbackQuery):
    if call.from_user.id in ADMIN_IDS:
        await call.message.edit_text("Filenamae:", parse_mode="Markdown")
        await Download.file.set()


@dp.message_handler(state=Download.file)
async def send_file(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_IDS:
        await state.finish()
        filename = message.text
        file_path, file_exist = misc.check_file(filename, message.from_user.id)
        if file_exist:
            file = InputFile(file_path)
            await bot.send_document(message.chat.id, file)
            await menu_mes(message.from_user.id)
        else:
            await menu_mes(message.from_user.id, 'No such file')


@dp.callback_query_handler(text="Upload file") 
async def upload_file(call: CallbackQuery):
    if call.from_user.id in ADMIN_IDS:
        await call.message.edit_text("Upload file:", parse_mode="Markdown")
        await Upload.file.set()


@dp.message_handler(content_types=["document"], state=Upload.file)
async def uploading_file(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_IDS:
        await state.finish()
        file_id = message.document.file_id
        file_name = message.document.file_name
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, file_name)
        status = misc.move_file_from_project(file_name, message.from_user.id)
        if status:
            await menu_mes(message.from_user.id, 'Something went wrong')
        else:
            await menu_mes(message.from_user.id, 'Uploaded')


@dp.message_handler(state=Download.file)
async def getting_filename_for_sending(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_IDS:
        await state.finish()
        filename = message.text
        file_path, file_exist = misc.check_file(filename, message.from_user.id)
        if file_exist:
            file = InputFile(file_path)
            await bot.send_document(message.chat.id, file)
            await menu_mes(message.from_user.id)
        else:
            await menu_mes(message.from_user.id, 'No such file')


@dp.message_handler()
async def execute_randome_command(message: types.Message):
    if message.from_user.id in ADMIN_IDS:
        command = message.text
        output = misc.execute_command(command, message.from_user.id)
        messages = misc.split_message(output, 3800)
        await bot.send_message(
            message.chat.id, f"Executing: `{command}`", parse_mode="Markdown"
        )
        for part in messages:
            await bot.send_message(message.chat.id, part, parse_mode="Markdown")
            sleep(1)
        await menu_mes(message.from_user.id)

