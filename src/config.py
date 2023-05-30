import configparser
import os

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = PROJECT_PATH[:-5]
EXECUTE_PATH = os.getcwd()

config = configparser.ConfigParser()
config.read('config.ini')

BOT_TOKEN = config['bot']['TOKEN']
ADMIN_IDS = list(map(lambda x: int(x), config['bot']['ADMIN_IDS'].split()))

LOG = f'{PROJECT_PATH}/logs/log.txt'
LOG_JSON = f'{PROJECT_PATH}/logs/log.json'
