import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))


def create_post(name, content):
    # Creating a connection to the DB.
    con = sql.connect(path.join(ROOT, 'database.db'))
    # Creating a 'cursor' to only grab the data requested rather than excessive data.
    cur = con.cursor()
    # Executing raw sql syntax, and replacing values with the desires variables.
    cur.execute('insert into posts(name, context) values(?, ?)',
                (name, content))
    # Committing to the DB, then closing the connection.
    con.commit()
    con.close()


def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    # Selecting all posts within the DB.
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
