class ParkingLot:
    slots_occupied = 0

    def __init__(self, number_of_slots: int) -> None:
        self.number_of_slots = number_of_slots
        self.parking_slot = dict((el, None) for el in range(1, number_of_slots+1))

    def park(self, registration_number: str, age: int) -> bool:
        if self.slots_occupied < self.number_of_slots:
            for slot_number, slot_detail in self.parking_slot.items():
                if slot_detail is None:
                    self.parking_slot[slot_number] = [registration_number, age]
                    self.slots_occupied += 1
                    print(self.parking_slot, self.slots_occupied)
                    return True
        else:
            print(f"Uhh Ohh! All slots are filled. Please try other Parking lot. Could not Park: {registration_number}")
            return False

    def get_slot_num_for_drivers_of_age(self, age: int) -> list:
        list_of_filtered_slots = []
        for slot_number, slot_detail in self.parking_slot.items():
            if slot_detail is not None and slot_detail[1] == age:
                list_of_filtered_slots.append(slot_number)
        return list_of_filtered_slots

    def get_vehicle_reg_num_for_drivers_of_age(self, age: int) -> list:
        list_of_filtered_slots = []
        for slot_number, slot_detail in self.parking_slot.items():
            if slot_detail is not None and slot_detail[1] == age:
                list_of_filtered_slots.append(slot_detail[0])
        return list_of_filtered_slots

    def get_slot_num_for_car_with_reg_num(self, reg_num: str) -> int:
        for slot_number, slot_detail in self.parking_slot.items():
            if slot_detail[0] == reg_num:
                return slot_number

    def leave(self, slot_number: int) -> bool:
        if self.parking_slot.get(slot_number) is None:
            print(f'Slot already vacant.')
        elif slot_number <= self.number_of_slots and self.parking_slot.get(slot_number):
            print(f"Thank you {self.parking_slot.get(slot_number)[0]} for using Squad parking lot."
                  f" We look forward to serve you again.")
            self.parking_slot[slot_number] = None
            self.slots_occupied -= 1
            return True
        else:
            print(f"Uhh Ohh! We are not that big. The {slot_number} does not exist.")
            return False

