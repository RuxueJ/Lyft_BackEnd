from datetime import datetime

from CarFactory import CarFactory
from car import Car
from engine.capulet_engine import CapuletEngine


class Calliope(Car):

    def __int__(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
