import re
import time
import signal
import sys
import threading
import pickle

quitProgram = False


# SIGINIT handler
def signalHandler(sig, frame):
    print('You pressed Ctrl+C')
    sys.exit(0)


def timer():
    return str(time.time() - startingTime)


signal.signal(signal.SIGINT, signalHandler)
x = 1


def errorMessage():
    print("can not open the file")
    return


class grouping(threading.Thread):

    def __init__(self, regEx, name):
        super(grouping, self).__init__()
        self.filename = open(sys.argv[1], 'r')
        self.regEx = regEx
        self.name = name

    def run(self):
        if self.filename.mode == 'r':

            # find regular expressions from the file
            urlAndDirectory = re.findall(
                self.regEx,
                self.filename.read())
            self.filename.close()

            # Opens pickle file and store the data
            pickle_out = open('data/' +
                              self.name +
                              '.pickle', 'wb')

            pickle.dump(urlAndDirectory,
                        pickle_out)

            # Closing pickle file.
            pickle_out.close()
            print('saved in data/' +
                  self.name +
                  '.pickle file ' +
                  'in ' +
                  timer() +
                  ' seconds')

        # handling errors
        else:
            self.filename.close()
            errorMessage()

    # close file properly if any disruption
    def __exit__(self):
        self.filename.opened_file.close()


while True:

    if len(sys.argv) <= 1:
        print('There is no argument after Python script.\n'
              'type \"python3 grouplisting.py there_some_file.txt\"')
        exit(1)
    else:
        startingTime = time.time()

        # Start threads, define regular expression and filename where, all the data must be store.
        directoryT = grouping('([a-z]+.+[a-z]+.[a-z]+/+[a-z]+/)', 'directory')
        fileNameT = grouping('([a-z]+.+[a-z]+.[a-z]+/+[a-z]+/+[a-z]+.+[a-z])', 'filename')
        queriesT = grouping('([a-z]+.+[a-z]+.[a-z]+\/+([a-z]+\?.*|\?.*))', 'queries')

        directoryT.start()
        fileNameT.start()
        queriesT.start()

        # Wtait till all the threads are finished then pause a program. In this case every 15 seconds.
        directoryT.join()
        fileNameT.join()
        queriesT.join()

        print("next check is after 15 second")
        time.sleep(15)

        if quitProgram:
            print("Process ended")
            break

print("exit")