from aiogram import Dispatcher, types
import re

from BotDB import sqlite_db


# @dp.message_handler(ignore_case=True, regexp=['\\d*\\sкалорий'])
async def exp_cal(message: types.Message):
    bot_dict = await sqlite_db.dict_factory()
    digit = re.match(r'\d*', message.text)
    cal_remains = int(bot_dict[0]) - int(digit.group())
    await message.reply(f'Твой остаток по калориям - {cal_remains} ккал')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(exp_cal,
                                regexp='\\d*\\sкалорий')
