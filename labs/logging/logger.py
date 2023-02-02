# import your libraries here.
from datetime import datetime
# the name of the log file to write to.
log_file = "log-file-2023-02-02.log"


def log(text, log_file=log_file):
    # open up the log file in the correct mode.
    f = open(log_file, 'a')

    # create a string that has the current date and time in the beginning of the text.
    f.write(f"[{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}]  {text}\n")

    # close the file.
    f.close()


def dump(log_file=log_file):
    '''
    This function prints out each line in the log file to the console
    '''
    # open up the log file in the correct mode.
    f = open(log_file, 'r')
    # read the file into a list.
    print(f.read())

    # iterate through each item in the list and print out the results.
    # close the file.
    f.close()
