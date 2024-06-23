#!/usr/bin/python3
""" This file reads the system stdin line-by-line
and parses it to retrieve some data """
import sys
import re
import signal


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
            r'^\S+ ?- ?\[\S+ \S+\] "GET /projects/260 HTTP/1.1"'
            r' (?P<status>\d{3}) (?P<size>\d+)$'
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

    def strRepresentation() -> None:
        """ prints the required information
        in the format <status code>: <number> """
        print("File size: {}".format(LogLine.total_size))
        for key in sorted(LogLine.status.keys()):
            value = LogLine.status[key]
            if value != 0:
                print("{}: {}".format(key, value))


def main() -> None:
    """ Main function """
    def signal_handler(sig, frame):
        pass

    signal.signal(signal.SIGINT, signal_handler)

    try:
        line_number = 0
        for line in sys.stdin:
            line_number += 1
            LogLine(line)
            if line_number == 10:
                line_number = 0
                LogLine.strRepresentation()
    except Exception:
        pass
    finally:
        LogLine.strRepresentation()
        sys.exit(0)


if __name__ == "__main__":
    main()
