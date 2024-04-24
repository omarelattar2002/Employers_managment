from flask import g
import sqlite3


def connect_to_database():
    sql = sqlite3.connect('C:/Users/omarf/Documents/coding_temple/week10/employers-managers/crudapplication.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_database():
    if not hasattr(g, 'crudapplication_db'):
        g.crudapplication_db = connect_to_database()
    return g.crudapplication_db