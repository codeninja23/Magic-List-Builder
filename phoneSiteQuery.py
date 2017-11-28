from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
# import phoneScrape
import csv
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

sitelist = input('Give me a file to eat: ')
updatedFile = input('Give me a file to poop: ')

with open(sitelist, newline='') as csvfile:
    sitereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in sitereader:
        print('-')
        print(row[0])
        site = row[0]
        try:
            f = urlopen('http://www.' + site)
            s = BeautifulSoup(f, 'html.parser')
            s = s.get_text()
            phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)
            dataStorage = [row[0]]
            if len(phone) == 0:
                dataStorage.appen('no phone')
                # print (" no phone,", end='')

            else :
                count = 1
                for item in phone:
                    dataStorage.append(item)
                    # print (item + ',', end='')

            if len(emails) == 0:
                dataStorage.append('no email')
                # print(" no email,", end='')

            else:
                count = 1
                for item in emails:
                    dataStorage.append(item)
                    # print(item + ',', end='')

            with open(updatedFile, "a", newline='') as out_file:
              wr = csv.writer(out_file)
              wr.writerow(dataStorage)
        except:
            print('skipped')
            pass
