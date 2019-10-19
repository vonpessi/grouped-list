import re
import time
import signal
import sys
import threading
import pickle

quitProgram = False


def signalHandler(sig, frame):
    print('You pressed Ctrl+C')
    sys.exit(0)


signal.signal(signal.SIGINT, signalHandler)
x = 1


def errorMessage():
    print("can not open the file")
    return


class directoryGroup(threading.Thread):

    def __init__(self):
        super(directoryGroup, self).__init__()
        self.filename = open(sys.argv[1], 'r')

    def run(self):
        if self.filename.mode == 'r':

            urlAndDirectory = re.findall(
                '([a-z]+.+[a-z]+.[a-z]+/+[a-z]+/)',
                self.filename.read())
            self.filename.close()

            pickle_out = open('data/directory.pickle', 'wb')
            pickle.dump(urlAndDirectory, pickle_out)
            pickle_out.close()
            print("saved in data/directory.pickle file")

        else:
            self.filename.close()
            errorMessage()

    def __exit__(self):
        self.filename.opened_file.close()


class filenameGroup(threading.Thread):

    def __init__(self):
        super(filenameGroup, self).__init__()
        self.filename = open(sys.argv[1], 'r')

    def run(self):
        if self.filename.mode == 'r':

            urlDirectoryFilename = re.findall(
                '([a-z]+.+[a-z]+.[a-z]+/+[a-z]+/+[a-z]+.+[a-z])',
                self.filename.read())
            self.filename.close()

            pickle_out = open('data/filename.pickle', 'wb')
            pickle.dump(urlDirectoryFilename, pickle_out)
            pickle_out.close()
            print("saved in data/filename.pickle file")

        else:
            self.filename.close()
            errorMessage()

    def __exit__(self):
        self.filename.opened_file.close()


class queriesGroup(threading.Thread):

    def __init__(self):
        super(queriesGroup, self).__init__()
        self.filename = open(sys.argv[1], 'r')

    def run(self):

        if self.filename.mode == 'r':
            queryString = re.findall(
                '([a-z]+.+[a-z]+.[a-z]+/+\?.*)',
                self.filename.read())
            self.filename.close()

            pickle_out = open('data/queries.pickle', 'wb')
            pickle.dump(queryString, pickle_out)
            pickle_out.close()
            print("saved in data/queries.pickle file")

        else:
            self.filename.close()
            errorMessage()

    def __exit__(self):
        self.filename.opened_file.close()


while True:

    startingTime = time.time()

    directoryT = directoryGroup()
    filenameT = filenameGroup()
    queriesT = queriesGroup()

    directoryT.start()
    filenameT.start()
    queriesT.start()

    print("finished in " +
          str(time.time() - startingTime) +
          " seconds")

    time.sleep(15)

    if quitProgram:
        print("Process ended")
        break

print("exit")
