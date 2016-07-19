
from base import conn, cursor

def create(content, userId):
    sql = "INSERT INTO posts (content, user_id) VALUES ('{}', '{}')".format(content, userId)
    cursor.execute(sql)
    conn.commit()
    return cursor.lastrowid


def findAll():
    sql = "SELECT p.content, u.full_name FROM posts AS p LEFT JOIN users AS u ON p.user_id = u.id"
    cursor.execute(sql)
    return cursor.fetchall()
