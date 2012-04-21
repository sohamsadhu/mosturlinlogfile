# Program to find the URLS that have been most referenced and used from a log file.
import sys

# Function that will quicksort the list of tuples that have occurence number as first
# element in tuple and the URL as the second element in the list. The list is sorted
# from the least referenced to most referenced as done in classical quicksort.
# From: www.algolist.net/Algorithms/Sorting/Quicksort
def sortDict(impurllist, left, right):
    i, j = left, right - 1
    pivot = impurllist[int((left + right) / 2)]
    while (i <= j):
        while (impurllist[i][0] < pivot[0]):
            i = i + 1
        while (impurllist[j][0] > pivot[0]):
            j = j - 1
        if (i <= j):
            temp = impurllist[i]
            impurllist[i] = impurllist[j]
            impurllist[j] = temp
            i = i + 1
            j = j - 1
    if (left < j):
        sortDict(impurllist, left, j)
    if (i < right):
        sortDict(impurllist, i, right)

# This function will take the dictionary and then convert the same to sorted list of
# tuple of URL and its respective number.
def sortLogDict(logdict):
    impurllist = []
    for entries in logdict: # Get the entries from dictionary into a tuple.
        entry = (logdict[entries], entries) 
        impurllist.append(entry)
    sortDict(impurllist, 0, len(impurllist))   # The tuple of URL list sent for sorting.
    return impurllist

# This function reads the log file and then returns the dictionary of URL as the key
# and the number of its appearence as the value in that dictionary. Note it is assumed
# that the log file is new line separated list of URLs.
def readLogFile(logfile):
    try:
        logfilehandle = open(logfile,'r')	# The read mode for reading of the file.
    except IOError:
        if IOError.errno == ENOENT :
            print("The said log file does not exist.")
            return None     # Since you cannot find file, return a None to say error.
        elif IOError.errno in (EACCES, EPERM):
            print('You do not have the permissions to read that file.')
            return None
        else:
            return None
    logfiledict = {}
    for lines in logfilehandle:
        line = lines.rstrip('\n')   # Make sure you remove the
        if line in logfiledict:
            urlhit = logfiledict.get(line)
            urlhit += 1
            logfiledict[line] = urlhit
        else:
            logfiledict[line] = 1
    logfilehandle.close()   # Close the log file
    return logfiledict      # Return the dictionary that is related to that log file.

# Show the URL from the last to the said number of URLS.
def showUrlLast(urllist, num):
    print('URL \t  \t \t References')
    if num > len(urllist):
        for element in reversed(urllist):
            print(str(element[1]), '\t', str(element[0]))
    else:
        j = -1
        for i in range(num):
            print(str(urllist[j][1]), '\t', str(urllist[j][0]))
            j = j - 1

# Definition of main.
def main():
    try:
        int(sys.argv[1])
    except ValueError:
        print('Please input a integer for the number of URLs you want to view.')
        return  # Terminate program execution if the arguments provided are not right.
    if len(sys.argv) != 3:
        print('Usage: python3.2 HighURLFinder.py #URLs_you_want Log_file')
        return
    else:
        logdict = readLogFile(sys.argv[2])
        if logdict is None:
            return  # Terminate execution since the file read program encountered error.
        else:
            impurllist = sortLogDict(logdict)
    showUrlLast(impurllist, int(sys.argv[1]))

# The starting point of the program
main()
