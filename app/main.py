import sys
import file_reader
import runner


def initialize_parking_lot(line):
    command, arg = file_reader.parse_line(line)
    return runner.create_parking_lot(command, arg)


if __name__ == '__main__':
    """
    python -m main ABSOLUTE_FILE_PATH or RELATIVE_FILE_PATH or 'tests/mocks/input.txt'
    """
    try:
        input_file = sys.argv[1]
    except (IndexError, NameError):
        print("Please pass a valid file to see how can I run Parking lot.")
        exit()

    with file_reader.read_file(input_file) as file:
        parking_lot = initialize_parking_lot(file.readline())
        for line in file:
            command, args = file_reader.parse_line(line)
            runner.execute_command(parking_lot, command, args)
