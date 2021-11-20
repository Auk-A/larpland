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
    c.execute("SELECT * FROM user_items")
    rows = c.fetchall()
    for row in rows:
        print(row)
    con.close()


def get_all_user_item_names():
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("SELECT name FROM user_items")
    names = c.fetchall()
    for name in names:
        print(name)
    con.close()


def get_random_weapon():
    con = sl.connect('data.db')
    c = con.cursor()

    c.execute("SELECT name FROM adjectives WHERE grammar = 1")
    prefixes = c.fetchall()
    prefix = random.choice(prefixes)

    c.execute("SELECT name FROM weapons")
    weapons = c.fetchall()
    weapon = random.choice(weapons)

    final = f'{"".join(prefix).capitalize()}  {"".join(weapon).capitalize()}'

    if round(random.random()):
        if round(random.random()):
            c.execute("SELECT name FROM adjectives WHERE grammar = 2")
            postfixes = c.fetchall()
            postfix = random.choice(postfixes)
            final = f'{final} of {"".join(postfix).capitalize()}'

        else:
            c.execute("SELECT name FROM mobs")
            mobs = c.fetchall()
            mob = random.choice(mobs)
            final = f'{final} of the {"".join(mob).capitalize()}'

    print(final)
