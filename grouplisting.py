import os
import re
import time
import signal
import sys
import threading
import csv
import datetime
from urllib.request import urlopen

quitProgram = False


# SIGINT handler
def signalHandler(sig, frame):
    print('You pressed Ctrl+C')
    sys.exit(0)


signal.signal(signal.SIGINT, signalHandler)
x = 1


def exitMessage():
    print('\nThere must be a three argument after Python script.\n\n'
          '$1 = list_of_urls\n'
          '$2 = list_of_regular_expressions\n'
          '$3 = csv_file_where_to_store_data\n\n'
          'for example\n\n'
          'python3 grouplisting.py example_list_of_urls.txt regex.csv data/saved_data.csv\n')
    sys.exit()


class checkUrlList(threading.Thread):

    def __init__(self):

        super(checkUrlList, self).__init__()

    def run(self):
        print('progressing...')
        if os.path.exists(sys.argv[1]):
            timeStamp = datetime.datetime.now()

            # open url file
            with open(sys.argv[1], 'r') as urlsFile:

                for url in urlsFile:
                    # add timestamp and url to the csv row.
                    newRow = [timeStamp, url.replace('\n', '')]

                    # open url and decode it to utf8 format
                    f = urlopen(url)
                    urlBytes = f.read()
                    urlText = urlBytes.decode("utf8")

                    t = threading.Thread(target=checkRegExFromUrl, args=(urlText, newRow))
                    t.start()
        else:
            print('file1 does not exist')


def checkRegExFromUrl(urlText, newRow):
    if os.path.exists(sys.argv[2]):

        # open regex file and csv.reader
        with open(sys.argv[2], 'r') as regExFile:
            csv_reader = csv.reader(regExFile)
            for regEx in csv_reader:
                reCompiledRegEx = re.compile(regEx[0])

                # check if the regex match  the url and gives boolean
                match = re.findall(regEx[0], urlText)
                if match:
                    newRow.append(True)
                else:
                    newRow.append(False)

        # write new row to the csv file
        with open(sys.argv[3], 'a') as f:
            writer = csv.writer(f)
            writer.writerow(newRow)

    else:
        print('file2 does not exist')
        exitMessage()


def writeHeader():

    if os.path.exists(sys.argv[3]):
        print(sys.argv[3] + ' exist')
    else:
        # write date and Url to the header
        csvFile = open(sys.argv[3], 'w')
        headerNameList = ['Date', 'Url']

        # opens regex file and check if there is a name for that
        # regular expression and write it to the header
        with open(sys.argv[2], 'r') as headerNames:
            csv_reader = csv.reader(headerNames)
            for headerName in csv_reader:
                if headerName[1] == '':
                    headerNameList.append(headerName[0])
                else:
                    headerNameList.append(headerName[1])

        writer = csv.DictWriter(
            csvFile, headerNameList)
        writer.writeheader()
        csvFile.close()


while True:

    if len(sys.argv) <= 3:
        exitMessage()
    else:

        writeHeader()

        checkUrlListThread = checkUrlList()
        checkUrlListThread.start()

        # Wait till all the threads are finished then pause a program. In this case every 15 seconds.
        checkUrlListThread.join()

        print('\nSearching is done and next check is starting after 15 second.\n'
              'you can cancel the operation for pressing Ctrl + C')
        time.sleep(15)

        if quitProgram:
            print('Process ended')
            break

print('exit')
