from parking_lot import ParkingLot
from vehicle import Vehicle

CREATE_PARKING_LOT = 'Create_parking_lot'
LEAVE = 'Leave'
PARK = 'Park'
SLOT_FOR_CAR_WITH_NUMBER = 'Slot_number_for_car_with_number'
SLOTS_FOR_DRIVER_OF_AGE = 'Slot_numbers_for_driver_of_age'
VEHICLE_REGISTRATION_NUMBERS_FOR_DRIVER_OF_AGE = 'Vehicle_registration_number_for_driver_of_age'


def create_parking_lot(command: str, args: list) -> ParkingLot:
    if command == CREATE_PARKING_LOT and len(args) == 1:
        slots = int(args[0])
        print(f'Creating Parking lot of {slots} slots.')
        return ParkingLot(slots)
    else:
        print('Could not create parking lot initially, you might miss some customers :(')
        exit(1)


def execute_command(parking_lot: ParkingLot, command: str, args: list) -> bool:
    if command == PARK and len(args) == 3:
        registration_number = args[0]
        driver_age = int(args[2])
        print(f'Park car with Vehicle Registration Number: {registration_number}, '
              f'and the car is driven by driver of Age : {driver_age}')
        parking_lot.park(Vehicle(registration_number, driver_age))
        return True

    elif command == LEAVE and len(args) == 1:
        slot = int(args[0])
        print(f'Vacating slot : {slot}')
        parking_lot.leave_from_slot(slot)
        return True

    elif command == SLOT_FOR_CAR_WITH_NUMBER and len(args) == 1:
        registration_number = args[0]
        slot = parking_lot.slot_number_by_registration_number(registration_number)
        print(f'The car {registration_number} is parked at {slot}')
        return True

    elif command == SLOTS_FOR_DRIVER_OF_AGE and len(args) == 1:
        driver_age = int(args[0])
        slot_list = parking_lot.slot_numbers_by_driver_age(driver_age)
        print(f'Slot Number List for Drivers of Age {driver_age} is {slot_list}')
        return True

    elif command == VEHICLE_REGISTRATION_NUMBERS_FOR_DRIVER_OF_AGE and len(args) == 1:
        driver_age = int(args[0])
        slot_list = parking_lot.vehicle_registration_numbers_by_driver_age(driver_age)
        print(f'Vehicle Number List for Drivers of Age {driver_age} is {slot_list}')
        return True

    return False
