import sqlite3 as db


# Создание двух таблиц для записи лимитов, вызывается при старте бота
def sql_start():
    global conn, cur
    conn = db.connect('calories.db')
    cur = conn.cursor()
    if conn:
        print('DB is OK!')
    conn.execute('CREATE TABLE IF NOT EXISTS general('
                 'id INTEGER PRIMARY KEY, '
                 'max_calories TEXT, '
                 'max_fats TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS support('
                 'id INTEGER PRIMARY KEY, '
                 'max_calories TEXT, '
                 'max_fats TEXT)')
    conn.commit()


# Добавление данных от пользователя в таблицы
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO general(id, max_calories, max_fats) '
                    'VALUES (?, ?, ?)', tuple(data.values()))
        cur.execute('INSERT INTO support(id, max_calories, max_fats) '
                    'VALUES (?, ?, ?)', tuple(data.values()))
        conn.commit()


# Создание словаря из колонок таблицы
def dict_factory(table_name: str, column_name: str, id):
    conn.row_factory = db.Row
    cur.execute(f'SELECT {column_name} FROM {table_name} WHERE id = {id}')
    data = cur.fetchall()
    return data


# Функция обнуления лимитов
async def rewriting(id):
    while True:
        gen = dict_factory('general',
                           'id, max_calories, max_fats', id)
        cur.execute(f'UPDATE support SET max_calories = { gen[0][1] }, '
                    f'max_fats = { gen[0][2] } '
                    f'WHERE id = { gen[0][0]}')
        conn.commit()
