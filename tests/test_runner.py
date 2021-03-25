import unittest

from squad_app.app.runner import *


def test_create_parking_lot():
    command = CREATE_PARKING_LOT
    args = [6]
    parking_lot_instance = create_parking_lot(command, args)
    assert isinstance(parking_lot_instance, ParkingLot)


def test_create_parking_lot_wrong_command():
    command = PARK
    args = [6]
    with unittest.TestCase.assertRaises(None, expected_exception=SystemExit) as cm:
        create_parking_lot(command, args)
    assert cm.exception.code == 1


def test_create_parking_lot_wrong_arguments():
    command = PARK
    args = [6, 7]
    with unittest.TestCase.assertRaises(None, expected_exception=SystemExit) as cm:
        create_parking_lot(command, args)
    assert cm.exception.code == 1


def test_execute_command_park():
    parking_lot = create_parking_lot(CREATE_PARKING_LOT, [3])
    execute_command(parking_lot, PARK, ['KA-01-HH-1234', 'driver_Age', 21])
    return parking_lot


def test_execute_command_park_wrong_args():
    parking_lot = create_parking_lot(CREATE_PARKING_LOT, [3])
    unittest.TestCase.assertFalse(None, execute_command(parking_lot, PARK, ['KA-01-HH-1234', 'driver_Age', 21, 24]))


def test_execute_command_leave():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertTrue(None, execute_command(parking_lot, LEAVE, [1]))


def test_execute_command_leave_wrong_args():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertFalse(None, execute_command(parking_lot, LEAVE, ['KA-01-HH-1234', 'driver_Age', 21, 24]))


def test_execute_command_slot_for_car_with_number():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertTrue(None, execute_command(parking_lot, SLOT_FOR_CAR_WITH_NUMBER, ['KA-01-HH-1234']))


def test_execute_command_slot_for_car_with_number_wrong_args():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertFalse(None, execute_command(parking_lot, SLOT_FOR_CAR_WITH_NUMBER, ['KA-01-HH-1234', 21]))


def test_execute_command_slots_for_driver_of_age():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertTrue(None, execute_command(parking_lot, SLOTS_FOR_DRIVER_OF_AGE, [21]))


def test_execute_command_slots_for_driver_of_age_wrong_args():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertFalse(None, execute_command(parking_lot, SLOTS_FOR_DRIVER_OF_AGE, [21, 22]))


def test_execute_command_vehicle_registration_number_by_driver_age():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertTrue(None, execute_command(parking_lot, VEHICLE_REGISTRATION_NUMBERS_FOR_DRIVER_OF_AGE, [21]))


def test_execute_command_vehicle_registration_number_by_driver_age_wrong_args():
    parking_lot = test_execute_command_park()
    unittest.TestCase.assertFalse(None, execute_command(parking_lot, VEHICLE_REGISTRATION_NUMBERS_FOR_DRIVER_OF_AGE, [2, 2]))


if __name__ == '__main__':
    unittest.main()
