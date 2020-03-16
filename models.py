import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_posts(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT into posts (name, content) values(?, ?)', (name, content))      # Is this vulnerable to SQL injection?
    con.commit()                # commit changes
    con.close()                 # close the connection to the DB

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts ')      # Is this vulnerable to SQL injection?
    posts = cur.fetchall()     # stores every db entry into tweets
    return posts

  