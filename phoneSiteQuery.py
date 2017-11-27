from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
# import phoneScrape
import csv
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

sitelist = input('Give me a file to eat: ')

with open(sitelist, newline='') as csvfile:
    sitereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in sitereader:
        print('-')
        print(row[0])
        site = row[0]
        try:
            f = urlopen('http://www.' + site)
#            print(f)
            s = BeautifulSoup(f, 'html.parser')
#            print(s)
            s = s.get_text()
            phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)

            if len(phone) == 0:
#               wr.writerow(['null'])
                print (" no phone,", end='')
                with open("out.csv", "a", newline='') as out_file:
                  wr = csv.writer(out_file)
                  wr.writerow([row[0],'null','phone number'])
            else :
                count = 1
                for item in phone:
#                    wr.writerow([item])
                    print (item + ',', end='')
                    count += 1
                    with open("out.csv", "a", newline='') as out_file:
                      wr = csv.writer(out_file)
                      wr.writerow([row[0],item,'phone number'])
            if len(emails) == 0:
#               wr.writerow(['null'])
                print(" no email,", end='')
                with open("out.csv", "a", newline='') as out_file:
                  wr = csv.writer(out_file)
                  wr.writerow([row[0],'null','email'])
            else:
                count = 1
                for item in emails:
#                    wr.writerow([item])
                    print(item + ',', end='')
                    count += 1
                    with open("out.csv", "a", newline='') as out_file:
                      wr = csv.writer(out_file)
                      wr.writerow([row[0],item,'email'])
        except:
            print('skipped')
            pass