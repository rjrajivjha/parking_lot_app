from vehicle import Vehicle
from typing import Optional


class ParkingLot:
    slots_occupied = 0

    def __init__(self, number_of_slots: int) -> None:
        self.number_of_slots = number_of_slots
        self.parking_slots = dict((el, None) for el in range(1, number_of_slots+1))

    def park(self, vehicle: Vehicle) -> bool:
        if self.__is_vehicle_parked(vehicle.registration_number):
            print(f"The Car with registration number: {vehicle.registration_number} is already parked.")
            return False

        if self.__is_parking_lot_full():
            print(f"Uhh Ohh! All slots are filled. Please try other Parking lot."
                  f" Could not Park: {vehicle.registration_number}")
            return False

        return self.__park_at_slot(vehicle, self.__next_available_slot())

    def leave_from_slot(self, slot: int) -> bool:
        if not self.__is_slot_occupied(slot):
            print(f'Slot already vacant.')
            return False
        if slot > self.number_of_slots or slot <= 0:
            print(f"Uhh Ohh! The {slot} does not exist.")
            return False

        return self.__leave(slot)

    def slot_numbers_by_driver_age(self, driver_age: int) -> list:
        list_of_filtered_slots = []
        for slot, vehicle in self.__occupied_slots().items():
            if vehicle.driver_age == driver_age:
                list_of_filtered_slots.append(slot)
        return list_of_filtered_slots

    def vehicle_registration_numbers_by_driver_age(self, driver_age: int) -> list:
        list_of_filtered_slots = []
        for slot in self.slot_numbers_by_driver_age(driver_age):
            vehicle = self.parking_slots.get(slot)
            list_of_filtered_slots.append(vehicle.registration_number)
        return list_of_filtered_slots

    def slot_number_by_registration_number(self, registration_number: str) -> int:
        for slot, vehicle in self.__occupied_slots().items():
            if vehicle.registration_number == registration_number:
                return slot
        return 0

    def __park_at_slot(self, vehicle: Vehicle, slot: int) ->bool:
        self.parking_slots[slot] = vehicle
        self.slots_occupied += 1
        print(f'Car with vehicle registration number "{vehicle.registration_number}" has been parked at '
              f'slot number {slot}')
        return True

    def __leave(self, slot: int) -> bool:
        vehicle = self.parking_slots.get(slot)
        print(f"Slot Number {slot} vacated, the car with registration number"
              f" {vehicle.registration_number} left the space, the driver of car was of age {vehicle.driver_age}")
        self.parking_slots[slot] = None
        self.slots_occupied -= 1
        return True

    def __is_parking_lot_full(self) -> bool:
        return self.slots_occupied == self.number_of_slots

    def __is_vehicle_parked(self, registration_number: str) -> bool:
        return self.slot_number_by_registration_number(registration_number) != 0

    def __next_available_slot(self) -> Optional[int]:
        for slot, vehicle in self.parking_slots.items():
            if vehicle is None:
                return slot
        return None

    def __occupied_slots(self) -> dict:
        return {slot: vehicle for slot, vehicle in self.parking_slots.items() if vehicle is not None}

    def __is_slot_occupied(self, slot: int) -> bool:
        return bool(self.parking_slots.get(slot))

