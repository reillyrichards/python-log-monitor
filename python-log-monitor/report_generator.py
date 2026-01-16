import csv
from event_detector import logdetection

def generate_report(output_file='report.csv'):
    suspicious_ip_counts, system_instability_events = logdetection()

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write Suspicious IPs section
        writer.writerow(['Suspicious IPs', 'Count'])
        for ip, count in suspicious_ip_counts.items():
            writer.writerow([ip, count])

        # Blank line between sections
        writer.writerow([])

        # Write System Instability Events section
        writer.writerow(['System Instability Events'])
        for event in system_instability_events:
            writer.writerow([event])
