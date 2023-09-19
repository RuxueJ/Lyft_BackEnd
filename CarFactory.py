from battery.nubbin_battery import NubbinBattery
from battery.splindler_battery import SplindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory():
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage):

        return Car(CapuletEngine(current_mileage,last_service_mileage), SplindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   SplindlerBattery(last_service_date, current_date))

    def create_palindrome(self, warning_light_is_on, last_service_date, current_date):
        return Car(SternmanEngine(warning_light_is_on),
                   SplindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))

