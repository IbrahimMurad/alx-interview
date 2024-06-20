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
            r'(\d{1,3}(\.\d{1,3}){3})'                           # IP address
            r' - '                                               # Separator
            r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]'  # Timestamp
            r' "GET /projects/260 HTTP/1.1"'                     # HTTP Method and URL and version
            r' (\d{3})'                                          # Status code
            r' (\d+)'                                            # Response size
        )
        isMatching = re.match(regex, line)

        if isMatching:
            status_code = int(isMatching.group(4))
            file_size = int(isMatching.group(5))
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
