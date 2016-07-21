import requests
import pyprind
from clint.textui import prompt

def download():
    url = 'http://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt'
    r = requests.get(url, stream=True)
    r.encoding = r.apparent_encoding
    file_size = int(r.headers.get('Content-Length', 0))
    print 'Downloading ' + url

    print 'File size: %s' % sizeof_fmt(file_size)

    content = ''

    bar = pyprind.ProgBar(file_size/1024, title='CVXNorm Codes')
    for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
        if chunk:
            content += chunk
            bar.update()


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def main():
    download()


if __name__ == '__main__':
    name = prompt.query('Where is your database?')
    inst_options = [{'selector': '1', 'prompt': 'Full', 'return': 'full'},
                    {'selector': '2', 'prompt': 'Partial', 'return': 'partial'},
                    {'selector': '3', 'prompt': 'None', 'return': 'no install'}]
    inst = prompt.options("Full or Partial Install", inst_options)

    main()
