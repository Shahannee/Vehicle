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

    def __init__(self, wheels, fuel_capacity, year, manufacturer, model_name):
        self._wheels = wheels
        self._fuel_capacity = fuel_capacity
        self._year = year
        self._manufacturer = manufacturer
        self._model_name = model_name

    def get_wheels_number(self):
        return self._wheels

    def get_fuel_capacity(self):
        return self._fuel_capacity

    def get_year(self):
        return self._year

    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def fuel(self, percent: FuelPercent):
        pass

    @abc.abstractmethod
    def get_wheels(self):
        pass

    @abc.abstractmethod
    def get_info(self):
        pass

class VehicleTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def create_vehicle(vehicle_type, fuel_capacity, year, manufacturer, model_name):
    if fuel_capacity <= 0 :
        raise ValueError("The fuel capacity must be a positive number.")
    if year <= 0 :
        raise ValueError("The year must be a positive number.")

    if vehicle_type is VehicleType.CAR:
        return Car(fuel_capacity, year, manufacturer, model_name)
    elif vehicle_type is VehicleType.MOTORCYCLE:
        return Motorcycle(fuel_capacity, year, manufacturer, model_name)
    else:
        raise VehicleTypeError("Invalid vehicle type. Please choose 'CAR' or 'MOTORCYCLE'.")


class Car(Vehicle):

    def __init__(self, fuel_capacity, year, manufacturer, model_name, wheels = 4):
        super().__init__(wheels, fuel_capacity, year, manufacturer, model_name)

    def drive(self):
        return "Driving a car."

    def fuel(self, percent):
        if not isinstance(percent, FuelPercent):
          raise ValueError(f"{percent} is invalid fuel percentage. Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL.")

        fuel_amount = self._fuel_capacity * percent.value
        return f"Filling {fuel_amount} liters of fuel."

    def get_wheels(self):
        return f"This {self._model_name} has {self._wheels} wheels."

    def get_info(self):
        return f"This {self._model_name} is made by {self._manufacturer} in {self._year}."


class Motorcycle(Vehicle):

    def __init__(self, fuel_capacity, year, manufacturer, model_name, wheels = 2):
        super().__init__(wheels, fuel_capacity, year, manufacturer, model_name)

    def drive(self):
        return "Driving a motorcycle."

    def fuel(self, percent):
        if not isinstance(percent, FuelPercent):
            raise ValueError("Invalid fuel percentage. Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL.")

        fuel_amount = self._fuel_capacity * percent.value
        return f"Filling {fuel_amount} liters of fuel."

    def get_wheels(self):
        return f"This {self._model_name} has {self._wheels} wheels."

    def get_info(self):
        return f"This {self._model_name} is made by {self._manufacturer} in {self._year}."