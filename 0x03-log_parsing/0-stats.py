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
        regex = r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
        match = re.match(regex, line)

        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            LogLine.total_size += file_size
            if status_code in LogLine.status.keys():
                LogLine.status[status_code] += 1
            

    def strRepresentation() -> str:
        """ returns the string representation of the class
        in the format <status code>: <number> """
        fileSize = "File size: {}\n".format(LogLine.total_size)
        status = ""
        for key, value in LogLine.status.items():
            if value != 0:
                status += "{}: {}\n".format(key, value)
        return fileSize + status


if __name__ == "__main__":
    line_number = 0
    try:
        for line in sys.stdin:
            line_number += 1
            try:
                LogLine(line)
                if line_number == 10:
                    line_number = 0
                    print(LogLine.strRepresentation(), end="")
            except (ValueError, SyntaxError):
                continue
    except KeyboardInterrupt:
        print(LogLine.strRepresentation(), end="")
