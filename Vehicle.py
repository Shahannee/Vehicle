from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"

class FuelPercent(Enum):
    ONE_QUARTER = 0.25
    HALF = 0.5
    THREE_QUARTERS = 0.75
    FULL = 1.0

class Vehicle(ABC):

    def __init__(self, wheels, fuel_capacity, year, manufacturer, model_name):
        self.wheels = wheels
        self.fuel_capacity = fuel_capacity
        self.year = year
        self.manufacturer = manufacturer
        self.model_name = model_name

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def fuel(self, percent: FuelPercent):
        pass

    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @staticmethod
    def create_vehicle(vehicle_type, wheels, fuel_capacity, year, manufacturer, model_name):
        """Method for creating vehicles with validation."""
        if vehicle_type == VehicleType.CAR:
            if wheels != 4 :
                raise ValueError("A car has 4 wheels.")
        elif vehicle_type == VehicleType.MOTORCYCLE:
            if wheels != 2:
                raise ValueError("A motorcycle has 2 wheels.")
        else:
            raise ValueError("Invalid vehicle type. Please choose 'CAR' or 'MOTORCYCLE'.")
        if fuel_capacity <= 0 :
            raise ValueError("The fuel capacity must be a positive number.")
        if year <= 0 :
            raise ValueError("The year must be a positive number.")

        if VehicleType == VehicleType.CAR:
            return Car(wheels, fuel_capacity, year, manufacturer, model_name)
        else:
            return Motorcycle(wheels, fuel_capacity, year, manufacturer, model_name)


class Car(Vehicle):

    def __init__(self, wheels, fuel_capacity, year, manufacturer, model_name):
        super().__init__(wheels, fuel_capacity, year, manufacturer, model_name)

    def drive(self):
        return "Driving a car."

    def fuel(self, percent: FuelPercent):
        if not isinstance(percent, FuelPercent):
          raise ValueError("Invalid fuel percentage. Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL.")

        fuel_amount = self.fuel_capacity * percent.value
        return f"Filling {fuel_amount} liters of fuel."

    def get_wheels(self):
        return f"This {self.model_name} has {self.wheels} wheels."

    def get_info(self):
        return f"This {self.model_name} is made by {self.manufacturer} in {self.year}."


class Motorcycle(Vehicle):

    def __init__(self, wheels, fuel_capacity, year, manufacturer, model_name):
        super().__init__(wheels, fuel_capacity, year, manufacturer, model_name)

    def drive(self):
        return "Driving a motorcycle."

    def fuel(self, percent: FuelPercent):
        if not isinstance(percent, FuelPercent):
            raise ValueError("Invalid fuel percentage. Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL.")

        fuel_amount = self.fuel_capacity * percent.value
        return f"Filling {fuel_amount} liters of fuel."

    def get_wheels(self):
        return f"This {self.model_name} has {self.wheels} wheels."

    def get_info(self):
        return f"This {self.model_name} is made by {self.manufacturer} in {self.year}."


car = (Vehicle.create_vehicle
    (VehicleType.CAR,
    4,
    50,
    2024,
    "Tesla",
    "Model S"))

car.drive()
car.get_wheels()
car.fuel(FuelPercent.HALF)
car.get_info()

motorcycle = (Vehicle.create_vehicle
    (VehicleType.MOTORCYCLE,
    2,
    15,
    2023,
    "Harley-Davidson",
    "Street Glide"))

motorcycle.drive()
motorcycle.get_wheels()
motorcycle.fuel(FuelPercent.HALF)
motorcycle.get_info()

