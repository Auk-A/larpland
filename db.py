import sqlite3 as sl


def start_connection():
    con = sl.connect('data.db')
