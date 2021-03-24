from squad_app.app.vehicle import Vehicle


class ParkingLot:
    slots_occupied = 0

    def __init__(self, number_of_slots: int) -> None:
        self.number_of_slots = number_of_slots
        self.parking_slot = dict((el, None) for el in range(1, number_of_slots+1))

    def park(self, vehicle: Vehicle) -> bool:
        if self.get_slot_num_for_car_with_reg_num(vehicle.registration_number) != 0:
            print(f"The Car with registration number: {vehicle.registration_number} is already parked.")
            return False
        if self.slots_occupied < self.number_of_slots:
            for slot_number, slot_detail in self.parking_slot.items():
                if slot_detail is None:
                    self.parking_slot[slot_number] = vehicle
                    self.slots_occupied += 1
                    print(f'Car with vehicle registration number "{vehicle.registration_number}" has been parked at slot number {slot_number}')
                    return True
        else:
            print(f"Uhh Ohh! All slots are filled. Please try other Parking lot. Could not Park: {vehicle.registration_number}")
            return False

    def get_slot_num_for_drivers_of_age(self, driver_age: int) -> list:
        list_of_filtered_slots = []
        for slot_number, vehicle in self.parking_slot.items():
            if vehicle is not None and vehicle.driver_age == driver_age:
                list_of_filtered_slots.append(slot_number)
        return list_of_filtered_slots

    def get_vehicle_reg_num_for_drivers_of_age(self, driver_age: int) -> list:
        list_of_filtered_slots = []
        for slot_number, vehicle in self.parking_slot.items():
            if vehicle is not None and vehicle.driver_age == driver_age:
                list_of_filtered_slots.append(vehicle.registration_number)
        return list_of_filtered_slots

    def get_slot_num_for_car_with_reg_num(self, reg_num: str) -> int:
        for slot_number, vehicle in self.parking_slot.items():
            if vehicle is not None and vehicle.registration_number == reg_num:
                return slot_number
            return 0

    def leave(self, slot_number: int) -> bool:
        vehicle = self.parking_slot.get(slot_number)
        if vehicle is None:
            print(f'Slot already vacant.')
        elif slot_number <= self.number_of_slots and vehicle:
            print(f"Slot Number {slot_number} vacated, the car with registration number {vehicle.registration_number} left the space,"
                  f"the driver of car was of age {vehicle.driver_age}")
            self.parking_slot[slot_number] = None
            self.slots_occupied -= 1
            return True
        else:
            print(f"Uhh Ohh! We are not that big. The {slot_number} does not exist.")
            return False

