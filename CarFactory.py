from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery, SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine,battery,tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        return Car(engine,battery,tires)

    @staticmethod
    def create_palindrome(warning_light_is_on, last_service_date, current_date, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine,battery,tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine,battery,tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        return Car(engine,battery,tires)

