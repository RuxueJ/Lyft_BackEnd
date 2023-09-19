from abc import ABC

from Serviceable import Serviceable


class Battery(Serviceable, ABC):
    def needs_service(self):
        pass
