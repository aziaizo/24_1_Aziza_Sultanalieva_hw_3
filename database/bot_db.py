import sqlite3
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.db")
    cursor=db.cursor()

    if db:
        print('База данных подключена')

    db.execute("CREATE TABLE IF NOT EXISTS SIMUS"
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name_admin TEXT, direction_admin TEXT, age_admin INTEGER,group_admin TEXT)")
    db.commit()

async def sql_command_insert(state):
    sql='''
    INSERT INTO SIMUS(name_admin,direction_admin,age_admin,group_admin)
    values(?,?,?,?)
    '''
    async with state.proxy() as data:
        cursor.execute(sql,tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM SIMUS").fetchall()
    random_user = random.choice(result)
    await message.answer(f" Имя:{random_user[1]}\n Направление:{random_user[2]}"
                             f" \n Возраст:{random_user[3]}\n Группа: {random_user[4]}")



async def sql_command_all():
    return cursor.execute("SELECT * FROM SIMUS").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM SIMUS WHERE id = ?", (user_id,))
    db.commit()


