
import MySQLdb
conn = MySQLdb.connect("localhost", "root", "root", "twitter_clone", 3306)
cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
