from aiogram import Bot
from pathlib import Path
from os import environ


BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / '.env'

# если env_path существует установит переменные среды в environ
if env_path.exists():
    with open(env_path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.strip().startswith('#'):
                continue
            name, value = line.strip().split('=', 1)
            environ[name] = value


TOKEN = environ.get('TOKEN')
ADMIN_ID = environ.get('ADMIN_ID')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT  10.0; Win64; x64; rv:58.0) '\
    'Gecko/20100101 Firefox/58.0'
}

bot = Bot(token=TOKEN)

bot_msg = {
    'stop_bot': 'Bot stopping',
    'start_bot': 'Bot starting',
}

CHIP_URL_BASE = environ.get('CHIP_URL_BASE')
