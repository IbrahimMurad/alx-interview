#!/usr/bin/python3
""" This file reads the system stdin line-by-line
and parses it to retrieve some data """
import sys
import re
import datetime


class LogLine:
    """ This class holds all the information required per line """

    total_size = 0
    status = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }

    def __init__(self, line: str) -> None:
        """ extracts the required information from the line """

        # splitting the line to get each part separately
        regex = (
            r'(?P<ip>\d{1,3}(\.\d{1,3}){3})'  # IP address
            r' - '                            # Separator
            r'\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]'  # Date
            r' "GET /projects/260 HTTP/1.1"'  # HTTP Request
            r' (?P<status>\d{3})'             # Status code
            r' (?P<size>\d+)'                 # File size
        )
        match = re.match(regex, line)

        try:
            if match:
                status_code = int(match.group('status'))
                file_size = int(match.group('size'))
                LogLine.total_size += file_size
                if status_code in LogLine.status.keys():
                    LogLine.status[status_code] += 1
        except Exception:
            pass

    def strRepresentation() -> str:
        """ returns the string representation of the class
        in the format <status code>: <number> """
        fileSize = "File size: {}\n".format(LogLine.total_size)
        status = ""
        for key in sorted(LogLine.status.keys()):
            value = LogLine.status[key]
            if value != 0:
                status += "{}: {}\n".format(key, value)
        return fileSize + status


if __name__ == "__main__":
    line_number = 0
    try:
        for line in sys.stdin:
            line_number += 1
            LogLine(line)
            if line_number == 10:
                line_number = 0
                print(LogLine.strRepresentation(), end="")
    except KeyboardInterrupt:
        print(LogLine.strRepresentation(), end="")
