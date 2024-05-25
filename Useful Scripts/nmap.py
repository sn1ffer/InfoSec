""""
nmap scanning from file list
"""

import subprocess as sub
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-O", "--output", help="Set path for output")
parser.add_argument("-T", "--target", help="Set targets")

args = parser.parse_args()

if args.output:
    outputfile = args.output

if args.target:
    target = args.target

def nmap(target, outputfile):
    with open(outputfile, 'a+') as out:
        with open(target) as target:
            lines = target.read().splitlines()

            for i in lines:
                print(i)

                sub.run(['sudo', 'nmap', '-A', '--script=vulners/vulners.nse', i], stdout=out)

nmap(target, outputfile)
