from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from BotDB import sqlite_db

scheduler = AsyncIOScheduler()


# Создаём состояние для хранения лимита калорий в оперативной памяти
class Preference(StatesGroup):
    id = State()
    max_calories = State()
    max_fats = State()


# Обработка команды /start и запуск отложенного обнуления лимитов
async def hello(message: types.Message):
    await message.answer('Привет! Введи команду /settings'
                         ' для установки лимита!')
    id = message.from_user.id
    scheduler.add_job(sqlite_db.rewriting, 'cron', [f'{id}'],
                      hour=2)


# Записываем калории
async def preference(message: types.Message):
    await message.answer('Установи свой лимит калорий.'
                         'Не бойся, я никому не скажу!')
    await Preference.max_calories.set()


async def process_max_calories_invalid(message: types.Message):
    return await message.reply('Введи числа, пожалуйста')


async def get_calories(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            await Preference.next()
            calories = int(message.text)
            id = message.from_user.id
            data['id'] = id
            data['max_calories'] = calories
            await message.reply(f'Понял. Твой лимит { message.text }.'
                                ' Теперь введи жиры.')
        except (ValueError, TypeError):
            await message.reply('Введи числа, пожалуйста')


# Записываем жиры и формируем словарь из полученных данных
async def process_max_fats_invalid(message: types.Message):
    return await message.reply('Ну числа же, ну')


async def get_fats(message: types.Message, state: FSMContext):
    try:
        fats = int(message.text)
        await state.update_data(max_fats=fats)
        await message.reply(f'Надо скушать { message.text } жиров. Понял')
        await sqlite_db.sql_add_command(state)
        await state.finish()
    except (ValueError, TypeError):
        await message.reply('Ну числа же, ну')


# Регистрация хэндлеров для соответствующих функция
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'], state=None)
    dp.register_message_handler(preference, commands=['settings'], state=None)
    dp.register_message_handler(process_max_calories_invalid,
                                lambda message: not message.text.isdigit(),
                                state=Preference.max_calories)
    dp.register_message_handler(get_calories,
                                lambda message: message.text.isdigit(),
                                state=Preference.max_calories)
    dp.register_message_handler(process_max_fats_invalid,
                                lambda message: not message.text.isdigit(),
                                state=Preference.max_fats)
    dp.register_message_handler(get_fats,
                                lambda message: message.text.isdigit(),
                                state=Preference.max_fats)
