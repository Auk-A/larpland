import random
import sqlite3 as sl


def check_player(name):
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("SELECT user.name FROM user WHERE user.name=?", [name])
    found = c.fetchone()
    con.commit()
    con.close()
    return bool(found)


# Kolommen kunnen wijzigen dus er wordt niet geïtereerd
def get_player(user_name):
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("SELECT user.name FROM user WHERE user.name=?", [user_name])
    found_name = c.fetchone()
    c.execute("SELECT user.level FROM user WHERE user.name=?", [user_name])
    found_level = c.fetchone()
    c.execute("SELECT user.health FROM user WHERE user.name=?", [user_name])
    found_health = c.fetchone()
    c.execute("SELECT user.coins FROM user WHERE user.name=?", [user_name])
    found_coins = c.fetchone()

    con.commit()
    con.close()

    player = {
        'name': found_name[0],
        'level': found_level[0],
        'health': found_health[0],
        'coins': found_coins[0]
    }

    return player


def create_player(user_name):
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("INSERT INTO user (name) VALUES(?)", [user_name])
    con.commit()
    con.close()
    print(f"Player {user_name} created")


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
    c.execute(query, [user_name])
    items = c.fetchall()
    for item in items:
        print(item)


def get_all_user_item_names():
    con = sl.connect('data.db')
    c = con.cursor()
    c.execute("SELECT user_item.name FROM user_item")
    names = c.fetchall()
    for name in names:
        print(name)
    con.close()


def get_random_weapon():
    con = sl.connect('data.db')
    c = con.cursor()

    c.execute("SELECT adjective.name FROM adjective WHERE grammar = 1")
    prefixes = c.fetchall()
    prefix = random.choice(prefixes)

    c.execute("SELECT weapon.name FROM weapon")
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
