import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_carrigan_tires_should_be_serviced(self):
        tire_wear = [1,1,1,0]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear = [0.5, 0.5, 0.1, 0.2]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())
