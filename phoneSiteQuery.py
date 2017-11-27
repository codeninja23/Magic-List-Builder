from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
# import phoneScrape
import csv
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

sitelist = input('Give me a file to eat: ')

resultFile = open("out.csv", "rb")
wr = csv.writer(resultFile, quotechar=',')

with open(sitelist, newline='') as csvfile:
    sitereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in sitereader:
        site = row[0]
        try:
            f = urlopen('http://www.' + site)
            s = BeautifulSoup(f, 'html.parser')
            s = s.get_text()
            phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)

            if len(phone) == 0:
                wr.writerow(['null'])
                print (" no phone,", end='')

            else :
                count = 1
                for item in phone:
                    wr.writerow([item])
                    print (item + ',', end='')
                    count += 1

            if len(emails) == 0:
                wr.writerow(['null'])
                print(" no email,", end='')
            else:
                count = 1
                for item in emails:
                    wr.writerow([item])
                    print(item + ',', end='')
                    count += 1
        except:
            print('skipped')
            pass

resultFile.close()

        #
        # except SSLError:
        #     print('shit')
        #     pass
        # except URLError:
        #     print('shit')
        #     pass
        # except HTTPError:
        #     print('shit')
        #     pass


        # print(', '.join(row))

        # with open(sitelist, newline='') as csvfile:
        #     sitereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     for row in sitereader:
        #         site = row[0]
        #         try:
                    # f = urlopen('http://www.' + site)
                    # s = BeautifulSoup(f, 'html.parser')
                    # s = s.get_text()
                    # phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
                    # emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)
        #
        #             if len(phone) == 0:
        #                 print (" no phone,", end='')
        #
        #             else :
        #                 count = 1
        #                 for item in phone:
        #                     print (item + ',', end='')
        #                     count += 1
        #
        #             if len(emails) == 0:
        #                 print(" no email,", end='')
        #             else:
        #                 count = 1
        #                 for item in emails:
        #                     print(item + ',', end='')
        #                     count += 1
        #         except:
        #             print('skipped')
        #             pass
