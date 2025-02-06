import abc as abc
import enum as enum

class VehicleType(enum.Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"

class FuelPercent(enum.Enum):
    ONE_QUARTER = 0.25
    HALF = 0.5
    THREE_QUARTERS = 0.75
    FULL = 1.0

class Vehicle:
    def __init__(self, wheels: int, fuel_capacity: int, year: int, manufacturer: str, model_name: str):
        self._wheels = wheels
        self._fuel_capacity = fuel_capacity
        self._year = year
        self._manufacturer = manufacturer
        self._model_name = model_name
        self._current_fuel = 0

    def set_current_fuel(self, fuel_amount: float) -> None:
        self._current_fuel = fuel_amount

    def get_fuel_capacity(self) -> int:
        return self._fuel_capacity

    def get_year(self) -> int:
        return self._year

    @abc.abstractmethod
    def drive(self) -> str:
        pass

    @abc.abstractmethod
    def fuel(self, percent: FuelPercent) -> str:
        pass

    @abc.abstractmethod
    def get_wheels(self) -> str:
        pass

    @abc.abstractmethod
    def get_info(self) -> str:
        pass

class VehicleTypeError(Exception):
    def __init__(self):
        message = "Invalid vehicle type. Please choose 'CAR' or 'MOTORCYCLE'."
        super().__init__(message)

class FuelCapacityError(Exception):
    def __init__(self):
        message = "The fuel capacity must be a positive number."
        super().__init__(message)

class InvalidYearError(Exception):
    def __init__(self):
        message = "The year must be a positive number."
        super().__init__(message)

def create_vehicle(vehicle_type, fuel_capacity, year, manufacturer, model_name):
    if fuel_capacity <= 0 :
        raise FuelCapacityError
    if year <= 0 :
        raise InvalidYearError

    if vehicle_type is VehicleType.CAR:
        return Car(fuel_capacity, year, manufacturer, model_name)
    elif vehicle_type is VehicleType.MOTORCYCLE:
        return Motorcycle(fuel_capacity, year, manufacturer, model_name)
    else:
        raise VehicleTypeError


class Car(Vehicle):
    def __init__(self, fuel_capacity, year, manufacturer, model_name):
        super().__init__(wheels = 4, fuel_capacity = fuel_capacity, year= year, manufacturer= manufacturer, model_name=model_name)

    def drive(self) -> str:
        return "Driving a car."

    def fuel(self, percent: FuelPercent) -> str:
        fuel_amount = self._fuel_capacity * percent.value
        self.set_current_fuel(fuel_amount = fuel_amount)
        return f"Filling {fuel_amount} liters of fuel."

    def get_wheels(self) -> str:
        return f"This {self._model_name} has {self._wheels} wheels."

    def get_info(self) -> str:
        return f"This {self._model_name} is made by {self._manufacturer} in {self._year}."


class Motorcycle(Vehicle):

    def __init__(self, fuel_capacity, year, manufacturer, model_name):
        super().__init__(wheels= 2, fuel_capacity= fuel_capacity, year= year, manufacturer= manufacturer, model_name= model_name)

    def drive(self) -> str:
        return "Driving a motorcycle."

    def fuel(self, percent : FuelPercent) -> str:
        fuel_amount = self._fuel_capacity * percent.value
        self.set_current_fuel(fuel_amount= fuel_amount)
        return f"Filling {fuel_amount} liters of fuel."

    def get_wheels(self) -> str:
        return f"This {self._model_name} has {self._wheels} wheels."

    def get_info(self) -> str:
        return f"This {self._model_name} is made by {self._manufacturer} in {self._year}."