import requests
import db


def init_db(conn):

    sql = """
    create table if not exists cvx_codes
    (
    code integer primary key,
    short_description text,
    full_vaccine_name text,
    notes text,
    status text,
    non_vaccine text,
    last_updated text
    )
    """
    conn.get_cursor().execute(sql)

    sql_index = """
    CREATE UNIQUE INDEX cvx_codes_PK ON cvx_codes (
    code
    )
    """
    conn.get_cursor().execute(sql_index)
    conn.commit()


def print_record(record):
    print 'CVXCode ' + record[0].strip()
    print 'ShortDescription ' + record[1].strip()
    print 'FullVaccineName ' + record[2].strip()
    print 'Notes ' + record[3].strip()
    print 'Status ' + record[4].strip()
    print 'NonVaccine ' + record[5].strip()
    print 'LastUpdated ' + record[6].strip()
    print '-----------------------------------------'


def insert_record(conn, record):

    values = \
        record[0].strip(), \
        record[1].strip(), \
        record[2].strip(), \
        record[3].strip(), \
        record[4].strip(), \
        record[5].strip(), \
        record[6].strip()

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


if __name__ == '__main__':
    main()
