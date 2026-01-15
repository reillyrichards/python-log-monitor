import ipaddress
from collections import defaultdict
from parser import logParse


def logdetection():
    valid_logs, invalid_logs = logParse()

    # Results
    suspicious_ip_counts = defaultdict(int)
    system_instability_events = []

    # Detection rules
    instability_keywords = {"timeout", "fail", "crash", "unusable", "disconnect"}

    for entry in valid_logs:
        level = entry[2]
        message = entry[3]
        words = message.split()

        # ---- Suspicious IP detection (ERROR + valid IP) ----
        if level == "ERROR" and words:
            candidate = words[-1]
            try:
                ip = ipaddress.ip_address(candidate)
                suspicious_ip_counts[str(ip)] += 1
            except ValueError:
                pass  # last token wasn't a valid IP

        # ---- System instability detection (case-insensitive) ----
        lowered_words = {word.lower() for word in words}
        if lowered_words & instability_keywords:
            system_instability_events.append(message)

    return dict(suspicious_ip_counts), system_instability_events


suspicious_ips, instability_events = logdetection()
print("Suspicious IPs:", suspicious_ips)
print("System instability events:", instability_events)
