CREATE_TABLE_REGISTRATIONTE = """
    CREATE TABLE IF NOT EXISTS registration
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id VARCHAR(255),
    firstname VARCHAR(255)
    )
"""

INSERT_INTO_TABLE_REGISTRATION = """
    INSERT INTO registration(telegram_id, firstname)
    VALUES (?, ?)
"""

CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    size VARCHAR(255),
    category VARCHAR(255),
    price VARCHAR(255),
    photo VARCHAR(255),
"""

INSERT_INTO_TABLE_PRODUCTS = """
    INSERT INTO products(telegram_id, firstname)
    VALUES (?, ?)
"""