from bot_logic.conf import bot, ADMIN_ID, bot_msg
from bot_logic.utils.commands import set_commands
from aiogram.enums import ParseMode
from aiogram.types import Message

from bot_logic.html_data import help_data, info_data 


async def start_bot():
    """Обработчик события запуска бота"""
    await set_commands(bot=bot)
    await bot.send_message(chat_id=ADMIN_ID, text=bot_msg['start_bot'])


async def stop_bot():
    """Обработчик события остановки бота"""
    
    await bot.send_message(chat_id=ADMIN_ID, text=bot_msg['stop_bot'])


async def help(message: Message):
    """Выведет список команд бота"""
    
    await message.answer(text=help_data, parse_mode=ParseMode.HTML)


async def info(message: Message):
    """Выведет информацию о боте"""
    
    await message.answer(text=info_data, parse_mode=ParseMode.HTML)
