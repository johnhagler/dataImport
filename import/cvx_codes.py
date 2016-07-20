import requests
import db
import utils


def init_db(conn):

    sql_drop = """
    DROP TABLE cvx_codes
    """
    print 'dropping table cvx_codes'
    conn.get_cursor().execute(sql_drop)

    sql_create = """
    CREATE TABLE cvx_codes (
    code              INTEGER PRIMARY KEY UNIQUE,
    short_description TEXT,
    full_vaccine_name TEXT,
    notes             TEXT,
    status            TEXT,
    non_vaccine       TEXT,
    last_updated      TEXT
    );
    """
    print 'creating table cvx_codes'
    conn.get_cursor().execute(sql_create)

    sql_index = """
    CREATE UNIQUE INDEX cvx_codes_PK ON cvx_codes (
    code
    );
    """
    print 'creating index cvx_codes_PK'
    conn.get_cursor().execute(sql_index)
    conn.commit()


def print_record(record):
    print '-----------------------------------------'
    print 'CVXCode ' + record[0].strip()
    print 'ShortDescription ' + record[1].strip()
    print 'FullVaccineName ' + record[2].strip()
    print 'Notes ' + record[3].strip()
    print 'Status ' + record[4].strip()
    print 'NonVaccine ' + record[5].strip()
    print 'LastUpdated ' + record[6].strip()


def insert_record(conn, record):

    update_date = utils.convert_date_format(record[6], '%Y/%m/%d', '%Y-%m-%d')

    values = \
        record[0].strip(), \
        record[1].strip(), \
        record[2].strip(), \
        record[3].strip(), \
        record[4].strip(), \
        record[5].strip(), \
        update_date

    sql = 'insert into cvx_codes values (?,?,?,?,?,?,?)'
    try:
        conn.get_cursor().execute(sql, values)
    except Exception as e:
        print e
    conn.commit()


def main(db_path):

    conn = db.Db(db_path)

    init_db(conn)

    r = requests.get('http://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt')
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    data = r.text

    lines = data.strip().split('\r')

    for line in lines:
        elements = line.split('|')
        if elements[0].strip().isnumeric():
            print_record(elements)
            insert_record(conn, elements)
