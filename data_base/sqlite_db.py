import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('bot.db')
    cur = base.cursor()
    if base:
        print('Database successfully connected!')
    base.execute('CREATE TABLE IF NOT EXISTS staff(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO staff VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM staff').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\n\nОписание: {ret[2]}\n\nЦена: {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM staff').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM staff WHERE name == ?', (data,))
    base.commit()

