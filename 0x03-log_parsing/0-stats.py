#!/usr/bin/python3
"""
This module is about log parsing in Python

"""
import sys

status_codes_count = {'200': 0,
                      '301': 0,
                      '400': 0,
                      '401': 0,
                      '403': 0,
                      '404': 0,
                      '405': 0,
                      '500': 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        parts = line.split(" ")

        if len(parts) > 4:
            status_code = parts[-2]
            file_size = int(parts[-1])

            if status_code in status_codes_count.keys():
                status_codes_count[status_code] += 1

            total_size += file_size
            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(total_size))

            for key, value in sorted(status_codes_count.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_count.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
