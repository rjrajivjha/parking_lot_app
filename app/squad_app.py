import sys

from squad_app.app.runner import execute_command, create_parking_lot
from squad_app.app.file_reader import parse_line, read_file


def initialize_parking_lot(line):
    return create_parking_lot(parse_line(line))


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
        parking_lot = initialize_parking_lot(file.readline())
        for line in file:
            command, *args = parse_line(line)
            execute_command(parking_lot, command, args)
