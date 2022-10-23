import re

from aiogram import Dispatcher, types

from BotDB import sqlite_db

from .stickers import send_random_stickers


class Measure:
    def __init__(self, value, name):
        self.value = value
        self.name = name

    async def send_remains(self, message: types.Message, column, eaten, id):
        mes_remains = self.value - eaten
        sqlite_db.cur.execute('UPDATE support '
                              f'SET {column} = {mes_remains} '
                              f'WHERE id = {id}')
        sqlite_db.conn.commit()
        if mes_remains >= 0:
            await message.reply(f'Твой остаток - {mes_remains} {self.name} ')
        else:
            send_random_stickers(message)


# Принимаем на вход сообщение, извлекаем цифру калорий или жиров,
# перезаписываем данные
async def exp_cal(message: types.Message):
    bot_dict = sqlite_db.dict_factory('support',
                                      'max_calories, max_fats',
                                      message.from_user.id)
    dig_in_mes = re.match(r'\d*', message.text)
    cal_val = int(bot_dict[0][0])
    fat_val = int(bot_dict[0][1])
    eaten = int(dig_in_mes.group())
    id = message.from_user.id
    if 'калор' in message.text.lower():
        calories = Measure(cal_val, 'ккал')
        await calories.send_remains(message, 'max_calories',
                                    eaten=eaten, id=id)
    elif 'жир' in message.text.lower():
        fats = Measure(fat_val, 'жиров')
        await fats.send_remains(message, 'max_fats', eaten=eaten, id=id)
    else:
        pass


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(exp_cal, regexp='\\d*\\sкалор|\\d*\\sжир')
