import os
import sys
from typing import IO

from constants import *
from parking_lot import ParkingLot


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


if __name__ == '__main__':
    """
    cd app
    python -m squad_app ABSOLUTE_FILE_PATH or RELATIVE_FILE_PATH or '../mocks/input.txt'
    """
    try:
        input_file = sys.argv[1]
    except (IndexError, NameError):
        print("Please pass a file to see how can I run Parking lot.")
        exit()

    with read_file(input_file) as file_handler:
        initial_command = file_handler.readline().strip().split(' ')
        parking_created_flag = False

        if initial_command[0] == CREATE_PARKING_LOT:
            print(f'Creating Parking lot with {initial_command[1]} slots.')
            parking_lot = ParkingLot(int(initial_command[1]))
            parking_created_flag = True
        else:
            print('Could not create parking lot initially, you might miss some customers :(')

        for line in file_handler:
            command = line.strip().split(' ')
            if command[0] == CREATE_PARKING_LOT and not parking_created_flag:
                parking_lot = ParkingLot(int(initial_command[1]))
                parking_created_flag = True
            elif parking_created_flag and command[0] == PARK and len(command) == 4:
                print(f'Park car with Vehicle Registration Number: {command[1]}, '
                      f'and the car is driven by driver of Age : {command[3]}')
                parking_lot.park(command[1], command[3])
            elif parking_created_flag and command[0] == LEAVE:
                print(f'Vacating slot : {command[1]}')
                parking_lot.leave(int(command[1]))
            elif parking_created_flag and command[0] == SLOT_NUMBER_FOR_CAR_WITH_NUMBER:
                slot_num = parking_lot.get_slot_num_for_car_with_reg_num(command[1])
                print(f'The car {command[1]} is parked at {slot_num}')
            elif parking_created_flag and command[0] == SLOT_NUMBERS_FOR_DRIVER_OF_AGE:
                slot_list = parking_lot.get_slot_num_for_drivers_of_age(command[1])
                print(f'Slot Number List for Drivers of Age {command[1]} is {slot_list}')
            elif parking_created_flag and command[0] == VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE:
                slot_list = parking_lot.get_vehicle_reg_num_for_drivers_of_age(command[1])
                print(f'Vehicle Number List for Drivers of Age {command[1]} is {slot_list}')
