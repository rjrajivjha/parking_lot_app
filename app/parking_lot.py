from squad_app.app.vehicle import Vehicle
import squad_app.app.commands as commands


class ParkingLot:
    slots_occupied = 0

    def __init__(self, number_of_slots: int) -> None:
        self.number_of_slots = number_of_slots
        self.parking_slot = dict((el, None) for el in range(1, number_of_slots+1))

    def is_parking_lot_full(self):
        return self.slots_occupied == self.number_of_slots

    def is_vehicle_parked(self, registration_number):
        return self.get_slot_for_car_with_reg_num(registration_number) != 0

    def next_available_slot(self):
        for slot, vehicle in self.parking_slot.items():
            if vehicle is None:
                return slot
        return None

    def park_at_slot(self, vehicle, slot):
        self.parking_slot[slot] = vehicle
        self.slots_occupied += 1
        print(f'Car with vehicle registration number "{vehicle.registration_number}" has been parked at slot number {slot}')
        return True

    def park(self, vehicle: Vehicle) -> bool:
        if self.is_vehicle_parked(vehicle.registration_number):
            print(f"The Car with registration number: {vehicle.registration_number} is already parked.")
            return False

        if self.is_parking_lot_full():
            print(f"Uhh Ohh! All slots are filled. Please try other Parking lot. Could not Park: {vehicle.registration_number}")
            return False

        return self.park_at_slot(vehicle, self.next_available_slot())


    def get_slots_for_drivers_of_age(self, driver_age: int) -> list:
        list_of_filtered_slots = []
        for slot, vehicle in self.parking_slot.items():
            if vehicle is not None and vehicle.driver_age == driver_age:
                list_of_filtered_slots.append(slot)
        return list_of_filtered_slots

    def get_vehicle_reg_nums_for_drivers_of_age(self, driver_age: int) -> list:
        list_of_filtered_slots = []
        for slot, vehicle in self.parking_slot.items():
            if vehicle is not None and vehicle.driver_age == driver_age:
                list_of_filtered_slots.append(vehicle.registration_number)
        return list_of_filtered_slots

    def get_slot_for_car_with_reg_num(self, reg_num: str) -> int:
        for slot, vehicle in self.parking_slot.items():
            if vehicle is not None and vehicle.registration_number == reg_num:
                return slot
            return 0

    def leave(self, slot: int) -> bool:
        vehicle = self.parking_slot.get(slot)
        if vehicle is None:
            print(f'Slot already vacant.')
        elif slot <= self.number_of_slots and vehicle:
            print(f"Slot Number {slot} vacated, the car with registration number {vehicle.registration_number} left the space,"
                  f"the driver of car was of age {vehicle.driver_age}")
            self.parking_slot[slot] = None
            self.slots_occupied -= 1
            return True
        else:
            print(f"Uhh Ohh! We are not that big. The {slot} does not exist.")
            return False

    def execute_command(self, command: str, args: list):
        if command == commands.PARK and len(args) == 3:
            print(f'Park car with Vehicle Registration Number: {args[0]}, '
                  f'and the car is driven by driver of Age : {args[2]}')
            self.park(Vehicle(args[0], int(args[2])))

        elif command == commands.LEAVE and len(args) == 1:
            print(f'Vacating slot : {args[0]}')
            self.leave(int(args[0]))

        elif command == commands.SLOT_FOR_CAR_WITH_NUMBER and len(args) == 1:
            slot = self.get_slot_for_car_with_reg_num(args[0])
            print(f'The car {args[0]} is parked at {slot}')

        elif command == commands.SLOTS_FOR_DRIVER_OF_AGE and len(args) == 1:
            slot_list = self.get_slots_for_drivers_of_age(args[0])
            print(f'Slot Number List for Drivers of Age {args[0]} is {slot_list}')

        elif command == commands.VEHICLE_REGISTRATION_NUMBERS_FOR_DRIVER_OF_AGE and len(args) == 1:
            slot_list = self.get_vehicle_reg_nums_for_drivers_of_age(args[0])
            print(f'Vehicle Number List for Drivers of Age {args[0]} is {slot_list}')


