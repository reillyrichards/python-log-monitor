from parser import logParse

#Logs any interesting events in the valid log files

def logdetection():
    valid, invalid = logParse()
    valid_ip_endings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    suspicious_IP = []
    system_instability_flags = ["timeout", "fail", "crash", "unusable", "disconnect"]
    system_instability = []

    for line in valid:
        message = line[3].split()

        if line[2] == "ERROR" and message[-1][0] in valid_ip_endings:
            suspicious_IP.append(message[-1])
        
        for word in message:
            if word in system_instability_flags:
                system_instability.append(message)
    
    return suspicious_IP, system_instability

logdetection()