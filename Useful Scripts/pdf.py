#Парсинг pdf 

#!/usr/bin/python3
from pdfminer.high_level import extract_text
from os import listdir
words = ['user','username','login','pass','password', 'passphere', 'secret']
files = listdir("./docs")
for filename in files:
    text = extract_text("./docs/"+filename)
    for word in words:
        if word in text:
            print("File: " + filename + " ============")
            print(text)
            break
