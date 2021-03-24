import unittest

from squad_app.app.parking_lot import ParkingLot
from squad_app.app.vehicle import Vehicle


class TestParkingLot(unittest.TestCase):
    num_of_slots = 3

    def setUp(self) -> None:
        self.parking = ParkingLot(self.num_of_slots)

    def test_park(self):
        vehicle = Vehicle('KA-01-HH-1234', 21)
        is_parked = self.parking.park(vehicle)
        self.assertTrue(is_parked)

    def test_re_park_same_vehicle_number(self):
        vehicle_1 = Vehicle('KA-01-HH-1234', 21)
        vehicle_2 = Vehicle('KA-01-HH-1234', 22)
        self.parking.park(vehicle_1)
        is_parked = self.parking.park(vehicle_2)
        self.assertFalse(is_parked)

    def test_park_full(self):
        vehicle_1 = Vehicle('KA-01-HH-1234', 21)
        vehicle_2 = Vehicle('KA-01-HH-1235', 22)
        vehicle_3 = Vehicle('KA-01-HH-1236', 22)
        vehicle_4 = Vehicle('KA-01-HH-1239', 22)
        self.parking.park(vehicle_1)
        self.parking.park(vehicle_2)
        self.parking.park(vehicle_3)
        is_parked = self.parking.park(vehicle_4)
        self.assertFalse(is_parked)


if __name__ == '__main__':
    unittest.main()


