from abc import ABC

from Serviceable import Serviceable


class Engine(Serviceable, ABC):
    def needs_service(self):
        pass
