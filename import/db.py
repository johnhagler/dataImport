import sqlite3


class Db(object):
    def __init__(self, db_path):
        print 'creating connection'
        self.conn = sqlite3.connect(db_path)

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def __del__(self):
        print 'closing connection'
        self.conn.close()
