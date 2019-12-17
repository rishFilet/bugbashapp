import sqlite3
from sqlite3 import Error

db_file = "/Users/rishi.k/rishi_code/bugbashapp/db.sqlite3"


class DB:
    def __init__(self):
        self.file = db_file
        self.conn = self.create_connection(self.file)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def find_name(self, first_name, last_name):
        exists = False
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM  "leaderboard_leaderboard" WHERE "first_name" = ? AND '
                    '"last_name"=?', (first_name, last_name,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

        if len(rows) > 0:
            exists = True

        return exists


DB().find_name("Rishi", "Khan")
