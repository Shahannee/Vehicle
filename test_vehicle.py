import unittest
from Vehicle import VehicleType, FuelPercent, Vehicle, Car, Motorcycle

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.car = Car(4,
                        50,
                        2024,
                        "Toyota",
                        "Corolla" )

        self.motorcycle = Motorcycle(2,
                                     15,
                                     2023,
                                     "Kawasaki",
                                     "Ninja 400")

    def test_create_vehicle(self):
        """Verifying positive test cases for creating a Car Vehicle."""
        self.assertIsInstance(self.car, Car)
        self.assertEqual(self.car.wheels, 4)
        self.assertGreater(self.car.fuel_capacity, 0)
        self.assertGreater(self.car.year, 0)

        """Verifying positive test cases for creating a Motorcycle Vehicle."""
        self.assertIsInstance(self.motorcycle, Motorcycle)
        self.assertEqual(self.motorcycle.wheels, 2)
        self.assertGreater(self.motorcycle.fuel_capacity, 0)
        self.assertGreater(self.motorcycle.year, 0)

        """Verifying error handling when unexpected values are given to the method."""
        with self.assertRaisesRegex(ValueError, "Invalid vehicle type. Please choose 'CAR' or 'MOTORCYCLE'."):
            Vehicle.create_vehicle("car", 4, 50, 2024, "Tesla", "Model S")

        with self.assertRaisesRegex(ValueError, "A car has 4 wheels."):
            Vehicle.create_vehicle(VehicleType.CAR, -5, 50, 2024, "Tesla", "Model S")

        with self.assertRaisesRegex(ValueError, "The fuel capacity must be a positive number."):
            Vehicle.create_vehicle(VehicleType.CAR, 4, -5, 2024, "Tesla", "Model S")

        with self.assertRaisesRegex(ValueError, "A motorcycle has 2 wheels."):
            Vehicle.create_vehicle(VehicleType.MOTORCYCLE, -2, 15, 2024, "Tesla", "Model S")


    def test_drive_car(self):
        expected_output = "Driving a car."
        self.assertEqual(self.car.drive(), expected_output)

    def test_drive_motorcycle(self):
        expected_output = "Driving a motorcycle."
        self.assertEqual(self.motorcycle.drive(), expected_output)

    def test_fuel_method_for_car(self):
        self.assertEqual(self.car.fuel_capacity * FuelPercent.FULL.value, 50)
        self.assertEqual(self.car.fuel_capacity * FuelPercent.THREE_QUARTERS.value, 37.5)
        self.assertEqual(self.car.fuel_capacity * FuelPercent.HALF.value, 25)
        self.assertEqual(self.car.fuel_capacity * FuelPercent.ONE_QUARTER.value, 12.5)

        """Verifying error handling when unexpected value is given to the method."""
        with self.assertRaisesRegex(ValueError, "Invalid fuel percentage. "
                                                "Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL."):
            self.car.fuel(50)


    def test_fuel_method_for_motorcycle(self):
        self.assertEqual(self.motorcycle.fuel_capacity * FuelPercent.FULL.value, 15)
        self.assertEqual(self.motorcycle.fuel_capacity * FuelPercent.THREE_QUARTERS.value, 11.25)
        self.assertEqual(self.motorcycle.fuel_capacity * FuelPercent.HALF.value, 7.5)
        self.assertEqual(self.motorcycle.fuel_capacity * FuelPercent.ONE_QUARTER.value, 3.75)

        """ Verifying error handling when unexpected value is given to the method."""
        with self.assertRaisesRegex(ValueError, "Invalid fuel percentage. "
                                                "Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL."):
            self.motorcycle.fuel(15)

    def test_get_info_car(self):
        self.assertEqual(self.car.get_info(), "This Corolla is made by Toyota in 2024.")

    def test_get_info_motorcycle(self):
        self.assertEqual(self.motorcycle.get_info(), "This Ninja 400 is made by Kawasaki in 2023.")

if __name__ == '__main__':
    unittest.main()