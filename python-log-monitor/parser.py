import re


#Parse function
def logParse():

    validloglevel = []
    invalidloglevel =[]
    try:
        logfile = open("../logsamples/app.log", "r")
        for line in logfile:
            line = line.split()
            if line[2] == 'INFO':
                validloglevel.append(line)
            elif line[2] == 'WARNING':
                validloglevel.append(line)
            elif line[2] == "ERROR":
                validloglevel.append(line)
            else:
                invalidloglevel.append(line)
        for log in validloglevel:
            join = ''.join(log[3:])
            log = log[:3]
            log.append(join)
            print(log)
    except FileNotFoundError:
        print("File cannot be found")

        return validloglevel

logParse()
