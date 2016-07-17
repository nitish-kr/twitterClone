
import MySQLdb
import config

conn = MySQLdb.connect(
    config.DB_HOST,
    config.DB_USER,
    config.DB_PASS,
    config.DB_NAME,
    config.DB_PORT
    )
cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
