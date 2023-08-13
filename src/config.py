import configparser
import os

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = PROJECT_PATH[:-3]
EXECUTE_PATH = os.getcwd()

config = configparser.ConfigParser()
config.read(f'{PROJECT_PATH}/config.ini')

BOT_TOKEN = config['bot']['TOKEN']
ADMIN_IDS = list(map(lambda x: int(x), config['bot']['ADMIN_IDS'].split()))

LOG = f'{PROJECT_PATH}/logs/remote_helper.log'
LOG_JSON = f'{PROJECT_PATH}/logs/remote_helper.log.json'
