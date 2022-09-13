import csv
import os
import subprocess as sub
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-O", "--output", help="Set path for output")

args = parser.parse_args()

if args.output:
    path = args.output

url = 'https://cve.mitre.org/data/downloads/allitems.csv'
filename = os.path.basename(url)

if os.path.exists(filename):
    os.remove(filename)
sub.run(['wget', '-O', filename, url])


with open(filename) as File:
    with open('allitems_utf.csv', mode="w+", encoding='utf-8', newline='') as allitems_utf:
        sub.run(['iconv', '-f', 'utf-8', '-t', 'utf-8', '-c', 'allitems.csv', '-o', 'allitems_utf.csv'])
        # sub.run(['iconv', '-f', '-utf-8', '-t', 'utf-8', '-c', str(filename), '-o', 'allitems_utf.csv'])

        with open('cve.csv', mode="w+", encoding='utf-8', newline='') as output_file:

            fieldnames = ['cve', 'description']
            writer = csv.DictWriter(output_file, delimiter=";", fieldnames=fieldnames)

            for i, line in enumerate(allitems_utf):

                if i > 10:
                    reader = csv.DictReader(allitems_utf, quoting=csv.QUOTE_ALL)
                    for row in reader:
                        values = list(row.values())
                        cve = values[0]
                        description = values[2]
                        writer.writerow({'cve': cve, 'description': description})

sub.run(['mv', 'cve.csv', path])