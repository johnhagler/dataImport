import sqlite3


class Db(object):
    def __init__(self, db_path):
        print 'creating connection'
        self.conn = sqlite3.connect(db_path)

    def execute_file(self, script_file, commit=True):
        with open(script_file) as f:
            content = f.read()
            scripts = content.split(';')
            for script in scripts:
                script = script.strip()
                if script:
                    print 'Executing script: %s' % script
                    self.conn.cursor().execute(script)
            if commit:
                self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.conn.cursor().execute('vacuum')
        self.conn.commit()
        print 'closing connection'
        self.conn.close()
