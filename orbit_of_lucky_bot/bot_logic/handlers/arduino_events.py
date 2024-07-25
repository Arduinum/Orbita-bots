from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from bot_logic.conf import CHIP_URL_BASE
from bot_logic.views import arduino_sections_list_view, \
    arduino_section_get_view
from bot_logic.utils.states_form import SendSectionStep


async def get_list_arduino_section_data_start(
        message: Message, 
        state: FSMContext
    ):
    """Ожидает ввода названия раздела для arduino"""

    await message.answer(
        text='Enter the section name or a word from the section.'
    )

    await state.set_state(state=SendSectionStep.get_section_from_arduino)


async def get_arduino_section_start(message: Message, state: FSMContext):
    """Ожидает ввода названия раздела для arduino"""

    await message.answer(
        text='Enter the section name or a word from the section.'
    )

    await state.set_state(state=SendSectionStep.get_section_from_arduino)


async def get_list_arduino_section_data(message: Message, state: FSMContext):
    """Выведет список данных из раздела arduino"""

    section = message.text

    section_url = arduino_section_get_view(
        base_url=CHIP_URL_BASE,
        section=section
    )

    if 'нет разделов' in section_url:
        await message.answer(text=section_url, parse_mode=ParseMode.HTML)
    else:
        
        state.clear()    


async def get_arduino_section(message: Message, state: FSMContext):
    """Выведет ссылку на раздел arduino"""

    section = message.text
    
    section_url = arduino_section_get_view(
        base_url=CHIP_URL_BASE,
        section=section
    )

    if 'нет разделов' in section_url:
        await message.answer(text=section_url, parse_mode=ParseMode.HTML)
    else:
        button = [InlineKeyboardButton(
            text=section_url['name'], 
            url=section_url['url']
        )]
        
        inline_kb = InlineKeyboardMarkup(inline_keyboard=[button])
        
        
        await message.answer(text='arduino section', reply_markup=inline_kb)
        await state.clear()


async def get_arduino_sections(message: Message):
    """Выведет список ссылок разделов arduino"""

    list_links = arduino_sections_list_view(base_url=CHIP_URL_BASE)
    text_links = ''.join(list_links)[:-1]
    
    await message.answer(
        text=text_links, 
        parse_mode=ParseMode.HTML, 
        disable_web_page_preview=True
    )
