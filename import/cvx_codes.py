import requests
import db
import utils
import pyprind


def init_db(conn):

    # sql_drop = """
    # DROP TABLE IF EXISTS cvx_codes
    # """
    # print 'dropping table cvx_codes'
    # conn.get_cursor().execute(sql_drop)
    #
    # sql_create = """
    # CREATE TABLE cvx_codes (
    # code              INTEGER PRIMARY KEY UNIQUE,
    # short_description TEXT,
    # full_vaccine_name TEXT,
    # notes             TEXT,
    # status            TEXT,
    # non_vaccine       TEXT,
    # last_updated      TEXT
    # );
    # """
    # print 'creating table cvx_codes'
    # conn.get_cursor().execute(sql_create)
    #
    # sql_index = """
    # CREATE UNIQUE INDEX cvx_codes_PK ON cvx_codes (
    # code
    # );
    # """
    # print 'creating index cvx_codes_PK'
    # conn.get_cursor().execute(sql_index)
    # conn.commit()

    conn.execute_file('db/schema.sql')


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


def get_cvx_data():
    r = requests.get('http://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt')
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    return r.text


def parse_cvx_data(data):

    parsed = []
    lines = data.strip().split('\r')

    for line in lines:
        elements = line.split('|')
        if elements[0].strip().isnumeric():
            parsed.append(elements)

    return parsed


def write_to_db(db_path, records):
    if records:
        conn = db.Db(db_path)
        init_db(conn)

        print 'Inserting records into database'
        for record in pyprind.prog_bar(records):
            insert_record(conn, record)
            #print_record(record)


def main(db_path):

    data = get_cvx_data()

    records = parse_cvx_data(data)

    write_to_db(db_path, records)



