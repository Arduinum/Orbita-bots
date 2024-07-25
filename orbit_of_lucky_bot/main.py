# библиотека для ассинхронной работы
from asyncio import run
# библиотека для работы с telegram
from aiogram import Dispatcher
from aiogram.filters import Command

from logging import basicConfig, INFO
from bot_logic.handlers.events import start_bot, stop_bot, help, info
from bot_logic.handlers.arduino_events import (
    get_arduino_sections,
    get_arduino_section_start, 
    get_arduino_section, 
    get_list_arduino_section_data_start,
    get_list_arduino_section_data
)
from bot_logic.conf import bot
from bot_logic.utils.states_form import SendSectionStep


async def start():
    basicConfig(
        level=INFO,
        format='%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).'
            '%(funcName)s(%(lineno)d) - %(message)s'
    )
    
    dp = Dispatcher()  #  поток обработки для входящих
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(
        help, 
        Command(commands='help')
    )
    
    dp.message.register(
        get_arduino_sections, 
        Command(commands='get_arduino_sections')
    )
    
    dp.message.register(
        get_arduino_section_start, 
        Command(commands='get_arduino_section')
    )

    dp.message.register(
        get_arduino_section, 
        SendSectionStep.get_section_from_arduino
    )

    dp.message.register(
        get_list_arduino_section_data_start, 
        Command(commands='get_list_arduino_section_data')
    )

    dp.message.register(
        get_list_arduino_section_data, 
        SendSectionStep.get_section_from_arduino
    )

    dp.message.register(
        info,
        Command(commands='info')
    )

    try:
        await dp.start_polling(bot)  # бесконечный цикл опроса событий
    finally:
        await bot.session.close()  # закрываем сессию


if __name__ == '__main__':
    run(start())
