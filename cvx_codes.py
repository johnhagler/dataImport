import requests

r = requests.get('http://www2a.cdc.gov/vaccines/iis/iisstandards/downloads/cvx.txt')
r.encoding = r.apparent_encoding
r.raise_for_status()
data = r.text

lines = data.strip().split('\r')

for line in lines:
    elements = line.split('|')
    if elements[0].strip().isnumeric():
        print 'CVXCode ' + elements[0].strip()
        print 'ShortDescription ' + elements[1].strip()
        print 'FullVaccineName ' + elements[2].strip()
        print 'Notes ' + elements[3].strip()
        print 'Status ' + elements[4].strip()
        print 'NonVaccine ' + elements[5].strip()
        print 'LastUpdated ' + elements[6].strip()
        print '-----------------------------------------'
