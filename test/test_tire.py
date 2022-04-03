import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 32300
        last_service_mileage = 10
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced(self):
        current_mileage = 32300
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternmanBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 62300
        last_service_mileage = 10
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced(self):
        current_mileage = 62300
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())