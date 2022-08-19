from distutils.util import execute
import sqlite3 as db


def sql_start():
    global conn, cur
    conn = db.connect('calories.db')
    cur = conn.cursor()
    if conn:
        print('DB is OK!')
    conn.execute('CREATE TABLE IF NOT EXISTS general('
                 'max_calories TEXT PRIMARY KEY, '
                 'max_fats TEXT)')
    conn.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO general VALUES (?, ?)', tuple(data.values()))
        conn.commit()


async def dict_factory():
    conn.row_factory = db.Row
    cur.execute('select * from general')
    data = cur.fetchone()
    return data
