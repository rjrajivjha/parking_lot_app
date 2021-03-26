import unittest
from squad_app.app.file_reader import *


def test_read_file():
    file_name = 'tests/mocks/input.txt'
    handler = read_file(file_name)
    assert True if handler else False


def test_read_wrong_file():
    file_name = 'inpu.txt'
    with unittest.TestCase.assertRaises(None, expected_exception=SystemExit) as cm:
        read_file(file_name)
    assert cm.exception.code == 1


def test_parse_line():
    line = 'Park KA-01-HH-1234 driver_age 21'
    command, args = parse_line(line)
    assert True if command == 'Park' else False
    assert True if args == ['KA-01-HH-1234', 'driver_age', '21'] else False


if __name__ == '__main__':
    unittest.main()


