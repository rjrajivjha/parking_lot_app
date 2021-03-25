import unittest

from squad_app.app.parking_lot import ParkingLot
from squad_app.app.vehicle import Vehicle


class TestParkingLot(unittest.TestCase):
    num_of_slots = 3

    def setUp(self) -> None:
        self.parking_lot = ParkingLot(self.num_of_slots)

    def set_up_full_parking(self):
        vehicles = [
            Vehicle('KA-01-HH-1234', 21),
            Vehicle('KA-01-HH-1235', 22),
            Vehicle('KA-01-HH-1236', 22),
        ]
        for vehicle in vehicles:
            self.parking_lot.park(vehicle)
        return self.parking_lot

    def test_park(self):
        vehicle = Vehicle('KA-01-HH-1234', 21)
        is_parked = self.parking_lot.park(vehicle)
        self.assertTrue(is_parked)

    def test_re_park_same_vehicle(self):
        vehicle_1 = Vehicle('KA-01-HH-1234', 21)
        vehicle_2 = Vehicle('KA-01-HH-1234', 22)
        is_parked_vehicle_1 = self.parking_lot.park(vehicle_1)
        is_parked_vehicle_2 = self.parking_lot.park(vehicle_2)
        self.assertTrue(is_parked_vehicle_1)
        self.assertFalse(is_parked_vehicle_2)

    def test_park_full(self):
        self.set_up_full_parking()
        test_vehicle = Vehicle('KA-01-HH-1239', 22)
        is_parked = self.parking_lot.park(test_vehicle)
        self.assertFalse(is_parked)

    def test_leave_from_slot(self):
        self.parking_lot = self.set_up_full_parking()
        self.assertTrue(self.parking_lot.leave_from_slot(2))

    def test_leave_from_vacant_slot(self):
        self.set_up_full_parking()
        self.assertTrue(self.parking_lot.leave_from_slot(2))
        self.assertFalse(self.parking_lot.leave_from_slot(2))

    def test_leave_from_non_existing_slot(self):
        self.set_up_full_parking()
        self.assertFalse(self.parking_lot.leave_from_slot(4))


if __name__ == '__main__':
    unittest.main()


