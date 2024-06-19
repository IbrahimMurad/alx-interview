#!/usr/bin/python3
""" This file reads the system stdin line-by-line
and parses it to retrieve some data """
import sys
import re
import datetime


class LogLine:
    """ This class holds all the information required per line """

    file_size = 0
    status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

    def __init__(self, line: str) -> None:
        """ extracts the required information from the line """

        # splitting the line to get each part separately
        parts = line.split(" ")

        # Building the regex expression for the IP
        IP_octet_re = "((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9]?[0-9]))"
        IP_re = re.compile("^(" + IP_octet_re + "\\.){3}" + IP_octet_re)
        IP_Address = parts[0]

        # skip the line if the IP part is not a valid IP
        if not IP_re.match(IP_Address):
            raise SyntaxError

        # if the date is not a valid datetime, an exception is raised
        date = datetime.datetime.fromisoformat(
            parts[2][1:] + " " + parts[3][:-2] + "0"
            )

        # checking the request part and raise an exception
        # if not in the provided syntax
        request = parts[4] + " " + parts[5] + " " + parts[6]
        if request != "\"GET /projects/260 HTTP/1.1\"":
            raise ValueError

        # check the status code and raise exception if not in the list provided
        statusCode = parts[7]
        if statusCode not in LogLine.status.keys():
            raise ValueError

        # updating the file size and the number of status codes received
        LogLine.file_size += int(parts[8])
        LogLine.status[statusCode] += 1

    def strRepresentation() -> str:
        """ returns the string representation of the class
        in the format <status code>: <number> """
        fileSize = "File size: {}\n".format(LogLine.file_size)
        status = ""
        for key, value in LogLine.status.items():
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
