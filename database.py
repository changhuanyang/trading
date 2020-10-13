#! /usr/bin/env python3
import sqlite3


def check_table_exist(conn, table_name):
    c = conn.cursor()

    # get the count of tables with the name
    c.execute(
        """ SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' """.format(
            table_name
        )
    )

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print("{} table exists.".format(table_name))
        return True
    else:
        print("{} table not exists.".format(table_name))
        return False


def get_table_columns(conn, table_name):

    cursor = conn.execute("select * from {}".format(table_name))
    names = list(map(lambda x: x[0], cursor.description))
    print(names)

