//Получение списка всех файлов и директорий системы с хешом и разрешениями 


import os
import argparse
import hashlib
import stat

parser = argparse.ArgumentParser()
parser.add_argument("-O", "--output", help="Set filename for output")
parser.add_argument("-P", "--path", help="Specify the path to the desired directory")

args = parser.parse_args()

if args.output:
    file = args.output
if args.path:
    path = args.path


def md5(fname):
    if os.path.isfile(fname) is True:

        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            hash = hash_md5.hexdigest()
            return hash

def getFilesAndDir(path, file):
    with open(file, 'w') as f:
        for address, dirs, files in os.walk(path):

            for name in files:
                file = os.path.join(address, name)
                permissions = stat.filemode(os.stat(file).st_mode)
                try:
                    print(file + ' ' + permissions + ' ' + md5(file) + '' + '\n')
                    f.write(file + ' ' + permissions + ' ' + md5(file) + '' + '\n')
                except:
                    continue


getFilesAndDir(path, file)
