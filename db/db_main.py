import sqlite3 as sq
from db import queries

db = sq.connect("db/db.sqlite3")
cur = db.cursor()


async def sql_creat():
    if db:
        print("База данных подключена")
    cur.execute(queries.CREATE_TABLE_PRODUCTS)
    cur.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)
    db.commit()


async def sql_insert_products(name, size, price, id_product, photo):
    cur.execute(queries.INSERT_PRODUCTS, (name, size, price, id_product, photo))
    db.commit()


async def sql_insert_products_detail(category, info_product, id_product):
    cur.execute(queries.INSERT_PRODUCTS_DETAILS, (category, info_product, id_product))
    db.commit()


async def sql_insert_products_collection(collection, id_product):
    cur.execute(queries.INSERT_PRODUCTS_COLLECTION, (collection, id_product))
    db.commit()
