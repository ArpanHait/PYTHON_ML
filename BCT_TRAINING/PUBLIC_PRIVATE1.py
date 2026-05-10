class Car:
    def __init__(self, brand, model, engine):
        self.brand=brand              #public attribute
        self._model=model             #protected attribute
        self.__engine=engine          #protected attribute

    def _show_details(self):          #protected method
        print(f"Brand:{self.brand}, Model: {self._model}, Engine:{self.__engine}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, "Electric")
        self.battery_capacity=battery_capacity

    def show_info(self):
        self._show_details()
        print(f"Battery:{self.battery_capacity}KWh")

tesla=ElectricCar("Tesla", "Model S", 100)
tesla.show_info()
print(tesla._model)