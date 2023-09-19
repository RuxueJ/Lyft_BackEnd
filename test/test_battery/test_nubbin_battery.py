import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        current_date  = date.fromisoformat("2023-09-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery( last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2023-09-15")
        last_service_date = date.fromisoformat("2022-01-25")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())