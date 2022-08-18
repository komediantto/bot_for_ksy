from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# Создаём состояние для хранения лимита калорий
class Preference(StatesGroup):
    max_calories = State()
    max_fats = State()


# Обработка команды /start
async def hello(message: types.Message):
    await message.answer('Привет! Введи команду /settings'
                         ' для установки лимита!')


# Записываем калории
async def preference(message: types.Message):
    await message.answer('Установи свой лимит калорий.'
                         'Не бойся, я никому не скажу!')
    await Preference.max_calories.set()


async def get_calories(message: types.Message,
                       state=Preference.max_calories):
    async with state.proxy() as data:
        try:
            calories = int(message.text)
            data['max_calories'] = calories
            await message.reply(f'Понял. Твой лимит { message.text }.'
                                'Теперь введи жиры.')
            await Preference.next()
        except (ValueError, TypeError):
            await message.reply('Введи числа, пожалуйста')


# Записываем жиры
async def get_fats(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            fats = int(message.text)
            data['max_fats'] = fats
            await message.reply(f'Надо скушать { message.text } жиров. Понял')
            await message.reply(str(data))
        except (ValueError, TypeError):
            await message.reply('Ну числа же, ну')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'], state=None)
    dp.register_message_handler(preference, commands=['settings'], state=None)
    dp.register_message_handler(get_calories, state=Preference.max_calories)
    dp.register_message_handler(get_fats, state=Preference.max_fats)
