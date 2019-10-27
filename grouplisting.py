import os
import re
import time
import signal
import sys
import threading
import csv
import datetime

quitProgram = False


# SIGINT handler
def signalHandler(sig, frame):
    print('You pressed Ctrl+C')
    sys.exit(0)


signal.signal(signal.SIGINT, signalHandler)
x = 1


def errorMessage():
    print("can not open the file")
    return


class grouping(threading.Thread):

    def __init__(self):
        super(grouping, self).__init__()

    def run(self):
        timeStamp = datetime.datetime.now()
        with open(sys.argv[1], 'r') as urlsFile:

            for url in urlsFile:
                newRow = [timeStamp, url.replace(' ', '').replace('\n', '')]
                with open(sys.argv[2], 'r') as regExFile:

                    for regEx in regExFile:
                        regEx = regEx.replace('\n', '')
                        reCompiledRegEx = re.compile(regEx)

                        match = re.search(reCompiledRegEx, url)
                        if match:
                            newRow.append(True)
                        else:
                            newRow.append(False)

                with open(sys.argv[3], 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(newRow)

        # Close file properly if any disruption

        def __exit__(self, exc_type, exc_value, traceback):
            for file in self.files:
                os.unlink(file)


def writeHeader():
    if os.path.exists(sys.argv[3]):
        return
    else:

        csvFile = open(sys.argv[3], 'w')
        headerNameList = ['Date', 'Url']

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
        print('\nThere must be three argument after Python script.\n\n'
              '$1 = list_of_urls\n'
              '$2 = list_of_regular_expressions\n'
              '$3 = csv_file_where_to_store_data\n\n'
              'for example\n\n'
              'python3 grouplisting.py urls.csv regexes.csv grouped_lists.csv\n')
        exit(1)
    else:

        writeHeader()

        groupingThread = grouping()
        groupingThread.start()

        # Wait till all the threads are finished then pause a program. In this case every 15 seconds.
        groupingThread.join()

        print("next check is after 15 second")
        time.sleep(15)

        if quitProgram:
            print("Process ended")
            break

print("exit")
