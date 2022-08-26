from aiogram import executor

from BotDB import sqlite_db
from create_bot import dp
from handlers import admin, other


async def start(_):
    print('Бот запущен')
    sqlite_db.sql_start()

admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

if __name__ == "__main__":
    # Запуск бота
    admin.scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=start)
