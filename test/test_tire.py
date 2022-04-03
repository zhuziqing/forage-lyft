import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.1, 0.5, 0.9]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.1, 0.6, 0.3]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.7, 0.8, 0.9]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.3, 0.2, 0.3, 0.4]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())