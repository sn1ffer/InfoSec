import calendar
import datetime
import csv
from api_response import result

date = datetime.datetime.utcnow()
utc_time = calendar.timegm(date.utctimetuple())

current_date = str(datetime.date.today())
file = 'Vulnerability_' + current_date + '.csv'

def last_vulns(file_name):

    message = ''
    count = 1
    with open(file_name, mode="w+", encoding='utf-8', newline='') as csv_file:

        fieldnames = ['Vulnerability', 'CVE', 'Risk']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for request in result:

            if str(datetime.datetime.utcfromtimestamp(
                    int(request.get('entry').get('timestamp').get('create'))).strftime('%Y-%m-%d')) \
                    == str(datetime.datetime.utcfromtimestamp(utc_time).strftime('%Y-%m-%d')) \
                    and str(request.get('vulnerability').get('risk').get('name')) != 'low':
                name = str(request.get('entry').get('title'))
                try:
                    cve = str(request.get('source').get('cve').get('id'))
                except:
                    cve = ''
                try:
                    risk = str(request.get('vulnerability').get('risk').get('name'))
                except:
                    risk = ''
                writer.writerow({'Vulnerability': name, 'CVE': cve, 'Risk': risk})

                count += 1

    return message


if __name__ == '__main__':
    print(last_vulns(file))
