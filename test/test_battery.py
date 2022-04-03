import unittest
from datetime import datetime

from battery.nubbinBattery import nubbinBattery
from battery.spindlerBattery import spindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        currentDate = date.fromisoformat("2022-03-02")
        lastServiceDate = date.fromisoformat("2015-03-09")
        battery = NubbinBattery(currentDate, lastServiceDate)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        currentDate = date.fromisoformat("2022-03-02")
        lastService_date = date.fromisoformat("2020-03-09")
        battery = NubbinBattery(currentDate, lastServiceDate)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        currentDate = date.fromisoformat("2022-03-02")
        lastServiceDate = date.fromisoformat("2019-03-09")
        battery = SpindlerBattery(currentDate, lastServiceDate)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        currentDate = date.fromisoformat("2022-03-02")
        lastServiceDate = date.fromisoformat("2021-03-09")
        battery = SpindlerBattery(currentDate,  lastServiceDate)
        self.assertFalse(battery.needs_service())
