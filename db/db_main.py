import sqlite3 as sq
from db import queries

db = sq.connect("db/db.splite3")
cur = db.cursor()


async def sql_creat():
    if db:
        print("База данных подключена")
    cur.execute(queries.CREATE_TABLE_REGISTRATIONTE)
    db.commit()


# async def sql_insert(telegram_id, ):
#     cur.execute(queries.INSERT_INTO_TABLE_REGISTRATION, __parameters=(telegram))