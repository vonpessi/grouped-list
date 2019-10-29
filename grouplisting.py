import os
import re
import signal
import time
import sys
import threading
import csv
import datetime
from urllib.request import urlopen

quitProgram = False

# Limit the number of parallel threads
semaphore = threading.Semaphore(5)
threads = []


# SIGINT handler
def signalHandler(sig, frame):
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

        print('you can cancel the process for pressing Ctrl + C.\n'
              'progressing...'
              'This might take a while...')

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

                    newThread = threading.Thread(target=checkRegExFromUrl, args=(urlText, newRow))

                    threads.append(newThread)
                    newThread.start()


        else:
            print('file1 does not exist')


def checkRegExFromUrl(urlText, newRow):
    semaphore.acquire()

    if os.path.exists(sys.argv[2]):

        # open regex file and csv.reader
        with open(sys.argv[2], 'r') as regExFile:
            csv_reader = csv.reader(regExFile)

            for regEx in csv_reader:

                # check if the regex match the url and gives boolean
                match = re.findall(regEx[0], urlText)
                if match:
                    newRow.append(True)
                else:
                    newRow.append(False)

        writeNewRowToCsv(newRow)

    else:
        print('file2 does not exist')
        exitMessage()


def writeNewRowToCsv(newRow):
    with open(sys.argv[3], 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newRow)
        time.sleep(1)
        semaphore.release()


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
        # Keyboard Interrupt
        try:
            checkUrlListThread = checkUrlList()
            checkUrlListThread.daemon = True
            checkUrlListThread.start()
            checkUrlListThread.join()

            while checkUrlListThread.is_alive():
                checkUrlListThread.join(1)
        except (KeyboardInterrupt, SystemExit):
            print('You shut down the process')
            sys.exit(0)

        # Wait till all the threads are finished then pause a program. In this case every 15 seconds.

        print('\nSearching is done and next check is starting after 15 second.\n'
              'you can cancel the process for pressing Ctrl + C')
        time.sleep(15)

        if quitProgram:
            print('Process ended')
            break

print('exit')
