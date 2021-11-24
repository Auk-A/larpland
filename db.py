import random
import sqlite3 as sl


def initialize_db():
    con = sl.connect('data.db')
    c = con.cursor()

    # values = ("Houten Zwaard", 3, 10)
    # c.execute("INSERT INTO weapons VALUES(null,?,?,?)", values)
    con.commit()
    con.close()


def get_all_user_items():
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("SELECT * FROM user_item")
    rows = c.fetchall()
    for row in rows:
        print(row)
    con.close()


def get_items_by_user_name(user_name):
    con = sl.connect('data.db')
    c = con.cursor()

    query = "select item.name, coin_value, speed, damage, range, item_type from user_item " \
            "JOIN user ON user.id=user_item.user_id " \
            "JOIN item ON item.id=user_item.item_id " \
            "WHERE user.name=?"
    param = user_name
    c.execute(query, param)


def get_all_user_item_names():
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("SELECT name FROM user_item")
    names = c.fetchall()
    for name in names:
        print(name)
    con.close()


def get_random_weapon():
    con = sl.connect('data.db')
    c = con.cursor()

    c.execute("SELECT name FROM adjective WHERE grammar = 1")
    prefixes = c.fetchall()
    prefix = random.choice(prefixes)

    c.execute("SELECT name FROM weapon")
    weapons = c.fetchall()
    weapon = random.choice(weapons)

    final = f'{"".join(prefix).capitalize()} {"".join(weapon).capitalize()}'

    if round(random.random()):
        if round(random.random()):
            c.execute("SELECT name FROM adjective WHERE grammar = 2")
            postfixes = c.fetchall()
            postfix = random.choice(postfixes)
            final = f'{final} of {"".join(postfix).capitalize()}'

        else:
            c.execute("SELECT name FROM mob")
            mobs = c.fetchall()
            mob = random.choice(mobs)
            final = f'{final} of the {"".join(mob).capitalize()}'

    return final
