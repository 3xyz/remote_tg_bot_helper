import os
import re
import subprocess

from loguru import logger

from src.config import ADMIN_IDS
from src.config import EXECUTE_PATH
from src.config import PROJECT_PATH

Dir = {}

for admin_id in ADMIN_IDS:
    Dir[admin_id] = EXECUTE_PATH


def serialize_path(text: str) -> str:
    return re.sub(r" ", r"\ ", text)


def remove_color_tags(text: str) -> str:
    return re.sub(r"\x1B\[([0-9]{1,3}(;[0-9]{1,2};?)?)?[mGK]", "", text)


def format_to_code(text: str) -> str:
    if len(text.strip().split("\n")) > 1:
        return "```\n" + text + "```"
    else:
        return "`" + text + "`"


def clean_up(text: str) -> str:
    text = text.replace("```", "")
    text = remove_color_tags(text)
    return text


def execute_command(command: str, user_id) -> str:
    pwd = Dir[user_id]
    result = ""
    result += format_to_code(pwd) + "\n"
    command_output = ""
    proc_out, proc_err, exit_code = run_subprocess(command, pwd)
    if exit_code:
        logger.info(f"Failed to execute: '{command}'")
        result += f"🔴  `$ {command}`\n"
    else:
        logger.info(f"Executed: '{command}'")
        result += f"🟢  `$ {command}`\n"
    result += "➖➖➖➖➖➖➖➖➖➖\n"
    if proc_out:
        command_output += proc_out
    if proc_err:
        command_output += "\nStderr:\n"
        command_output += proc_err
    if not command_output:
        command_output = "Empty"
    command_output = clean_up(command_output)
    result += format_to_code(command_output)
    print(result)
    return result


def split_message(message: str, limit: int = 3000) -> list[str]:
    messages = [""]
    current = 0
    length = 0
    for line in message.split("\n"):
        if limit > length + len(line):
            messages[current] = messages[current] + line + "\n"
            length += len(line)
        elif len(line) > limit:
            current += 1
            length = 0
            skip = f"Line {current} was skipped because is longer than {limit} chars"
            messages.append(skip + "\n")
            length += len(line)
        else:
            messages[current] = messages[current] + "```"
            length += len(line)
            current += 1
            length = 0
            messages.append("```" + line + "\n")
            length += len(line)
    return messages


def run_subprocess(command: str, pwd: str) -> tuple:
    proc = subprocess.run(
        [command],
        capture_output=True,
        text=True,
        shell=True,
        cwd=pwd,
    )
    proc_out = proc.stdout
    proc_err = proc.stderr
    exit_code = proc.returncode
    return proc_out, proc_err, exit_code


def get_path(filename: str, admin_id: int) -> str:
    file_path = ""
    if filename[0] != "/":
        file_path = Dir[admin_id] + "/" + filename
    else:
        file_path = filename
    return file_path


def check_file(filename: str, admin_id: int) -> tuple[str, bool]:
    file_exist = False
    file_path = get_path(filename, admin_id)
    if os.path.exists(file_path):
        file_exist = True
    return file_path, file_exist


def change_dir(path: str, user_id: int) -> int:
    status = 0
    pwd = Dir[user_id]
    if path[0] != "/":
        path = pwd + "/" + path
    if os.path.exists(path):
        proc2 = subprocess.run(
            ["pwd"],
            capture_output=True,
            text=True,
            cwd=path,
        )
        pwd_new = proc2.stdout
        Dir[user_id] = pwd_new.strip()
        status = 1
    return status


def move_file_from_project(file_name, user_id):
    status = 0
    file_path = PROJECT_PATH + file_name
    file_path = serialize_path(file_path)
    dest_path = Dir[user_id]
    dest_path = serialize_path(dest_path)
    if PROJECT_PATH[:-1] != dest_path:
        status = subprocess.run(f'mv {file_path} {dest_path}',
                                shell=True).returncode
    return status
