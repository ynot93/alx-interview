#!/usr/bin/python3
"""
This module deals with log parsing in Python

"""
import sys
import signal

total_file_size = 0
status_code_counts = {}
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_metrics():
    """
    Prints the current metrics

    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """
    Handles keyboard interruption signal

    """
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            ip = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if status_code not in valid_status_codes:
                continue

            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics()

        except ValueError:
            continue

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
