import os
import sys
from typing import IO

from parking_lot import ParkingLot
from squad_app.app.commands import CREATE_PARKING_LOT


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


def parse_parking_lot_creation(line):
    first_command, *slots = parse_line(line)
    if first_command == CREATE_PARKING_LOT and len(slots) == 1:
        return int(slots[0])
    else:
        print('Could not create parking lot initially, you might miss some customers :(')
        exit(1)


def create_parking_lot(slots):
    print(f'Creating Parking lot of {slots} slots.')
    return ParkingLot(slots)


if __name__ == '__main__':
    """
    python -m squad_app ABSOLUTE_FILE_PATH or RELATIVE_FILE_PATH or '../mocks/input.txt'
    """
    try:
        input_file = sys.argv[1]
    except (IndexError, NameError):
        print("Please pass a file to see how can I run Parking lot.")
        exit()

    with read_file(input_file) as file:
        slots = parse_parking_lot_creation(file.readline())
        parking_lot = create_parking_lot(slots)
        for line in file:
            command, *args = parse_line(line)
            parking_lot.execute_command(command, args)
