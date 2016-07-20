from datetime import datetime


def convert_date_format(value, from_format, to_format):
    dt = datetime.strptime(value, from_format)
    return dt.strftime(to_format)
