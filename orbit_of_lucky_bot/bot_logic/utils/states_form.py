from aiogram.fsm.state import StatesGroup, State


class SendSectionStep(StatesGroup):
    get_section_from_arduino = State()
