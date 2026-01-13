#Parse function
def logParse():

    valid_levels = ['INFO', 'WARNING', 'ERROR'] #Added to reduce IF statements
    valid = [] #reduces confusion in renaming
    invalid =[] 
    try:
        with open ("../logsamples/app.log", "r") as logfile:
            for line in logfile:
                line = line.split()
                if len(line) < 4: #Added incase structuring is different between log messages
                    invalid.append(line)
                    continue
                level = line[2]
                message = " ".join(line[3:])

                log_entry = line[:3] + [message]
                if level in valid_levels:
                    valid.append(log_entry)
                else:
                    invalid.append(log_entry)
    except FileNotFoundError:
        print("File cannot be found")
    return valid, invalid
