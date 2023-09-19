from battery.Battery import Battery


class SplindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date >
                self.last_service_date.replace(year=self.last_service_date.year + 2))