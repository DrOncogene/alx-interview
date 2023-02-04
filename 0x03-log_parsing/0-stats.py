#!/usr/bin/python3
"""
log parsing
"""
import sys
import re


format_regex = re.compile(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)')

CURR_SIZE = 0
CODES = {
  '200': 0,
  '301': 0,
  '400': 0,
  '401': 0,
  '403': 0,
  '404': 0,
  '405': 0,
  '500': 0
}


def update_stats(lines):
    """
    updates global log stats
    """
    global CODES
    for line in lines:
        code = line[2]
        if code in CODES:
            CODES[code] += 1


def print_stats():
    """prints stats"""
    print(f'File size: {CURR_SIZE}')
    for code, count in CODES.items():
        print(f'{code}: {count}')


def main():
    """main function"""
    lines = []
    global CURR_SIZE
    for line in sys.stdin:
        res = format_regex.findall(line.rstrip())
        if len(res) == 0:
            continue
        lines.append(res[0])
        CURR_SIZE += int(res[0][-1])
        if len(lines) == 10:
            update_stats(lines)
            print_stats()
            lines = []


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_stats()
        sys.exit(1)
