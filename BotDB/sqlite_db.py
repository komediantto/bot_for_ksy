import sqlite3 as db


def sql_start():
    global conn, cur
    conn = db.connect('calories.db')
    cur = conn.cursor()
    if conn:
        print('DB is OK!')
    conn.execute('CREATE TABLE IF NOT EXISTS general('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'max_calories TEXT, '
                 'max_fats TEXT)')
    conn.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO general(max_calories, max_fats) '
                    'VALUES (?, ?)', tuple(data.values()))
        conn.commit()


async def change_limit_cal():
    cur.execute('UPDATE general SET max_calories WHERE id = 1')


async def dict_factory():
    conn.row_factory = db.Row
    cur.execute('SELECT max_calories FROM general WHERE id = 1')
    data = cur.fetchone()
    return data
