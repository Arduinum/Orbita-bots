from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    """Команды для бота"""

    commands = [
        BotCommand(
            command='start',
            description='Start working bot'
        ),
        BotCommand(
            command='get_arduino_sections',
            description='Get list of Arduino data'
        ),
        BotCommand(
            command='get_arduino_section',
            description='Get link of Arduino data'
        ),
        BotCommand(
            command='get_list_arduino_section_data',
            description='get list arduino data from section'
        ),
        BotCommand(
            command='help',
            description='Get bot commands'
        ),
        BotCommand(
            command='info',
            description='Get information about the bot'
        )
        
    ]

    await bot.set_my_commands(
        commands=commands, 
        scope=BotCommandScopeDefault()
    )
