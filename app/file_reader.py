import os
from typing import IO


def read_file(file_name: str) -> IO:
    try:
        if os.path.getsize(file_name) == 0:
            print('File is empty')
            exit()
        return open(file_name)
    except FileNotFoundError as msg:
        # Custom exception
        print('The file does not exist, please try again.', msg)
        exit()


def parse_line(line):
    command, *args = line.strip().split(' ')
    return command, args