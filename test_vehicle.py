import unittest
import vehicle as ve
from vehicle import FuelCapacityError, InvalidYearError


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self._car = ve.Car(50,
                            2024,
                            "Toyota",
                            "Corolla" )

        self._motorcycle = ve.Motorcycle(15,
                                            2023,
                                            "Kawasaki",
                                            "Ninja 400")

    def test_create_car_vehicle(self):
        """Verifying positive test cases for creating a Car Vehicle."""
        self.assertIsInstance(self._car, ve.Car)
        self.assertEqual(self._car._wheels, 4)
        self.assertGreater(self._car._fuel_capacity, 0)
        self.assertGreater(self._car._year, 0)

    def test_create_motorcycle_vehicle(self):
        """Verifying positive test cases for creating a Motorcycle Vehicle."""
        self.assertIsInstance(self._motorcycle, ve.Motorcycle)
        self.assertEqual(self._motorcycle._wheels, 2)
        self.assertGreater(self._motorcycle._fuel_capacity, 0)
        self.assertGreater(self._motorcycle._year, 0)

    def test_invalid_vehicle_type_error_handling(self):
        """Verifying error handling when unexpected values are given to the method."""
        with self.assertRaisesRegex(ve.VehicleTypeError, "Invalid vehicle type. Please choose 'CAR' or 'MOTORCYCLE'."):
            ve.create_vehicle("car", 50, 2024, "Tesla", "Model S")

    def test_invalid_fuel_capacity_error_handling(self):
        with self.assertRaisesRegex(FuelCapacityError, "The fuel capacity must be a positive number."):
            ve.create_vehicle(ve.VehicleType.CAR, -5, 2024, "Tesla", "Model S")

    def test_invalid_year_error_handling(self):
        with self.assertRaisesRegex(InvalidYearError, f"The year must be a positive number."):
            ve.create_vehicle(ve.VehicleType.CAR, 50, -2024, "Tesla", "Model S")

    def test_drive_car(self):
        expected_output = "Driving a car."
        self.assertEqual(self._car.drive(), expected_output)

    def test_drive_motorcycle(self):
        expected_output = "Driving a motorcycle."
        self.assertEqual(self._motorcycle.drive(), expected_output)

    def test_fuel_method_for_car(self):
        self.assertEqual(self._car.fuel(ve.FuelPercent.FULL),  "Filling 50.0 liters of fuel.")
        self.assertEqual(self._car.fuel(ve.FuelPercent.THREE_QUARTERS),  "Filling 37.5 liters of fuel.")
        self.assertEqual(self._car. fuel(ve.FuelPercent.HALF),  "Filling 25.0 liters of fuel.")
        self.assertEqual(self._car. fuel(ve.FuelPercent.ONE_QUARTER),  "Filling 12.5 liters of fuel.")

    def test_fuel_method_for_motorcycle(self):
        self.assertEqual(self._motorcycle.fuel(ve.FuelPercent.FULL),  "Filling 15.0 liters of fuel.")
        self.assertEqual(self._motorcycle.fuel(ve.FuelPercent.THREE_QUARTERS),  "Filling 11.25 liters of fuel.")
        self.assertEqual(self._motorcycle.fuel(ve.FuelPercent.HALF),  "Filling 7.5 liters of fuel.")
        self.assertEqual(self._motorcycle.fuel(ve.FuelPercent.ONE_QUARTER),  "Filling 3.75 liters of fuel.")

    def test_get_info_car(self):
        self.assertEqual(self._car.get_info(), "This Corolla is made by Toyota in 2024.")

    def test_get_info_motorcycle(self):
        self.assertEqual(self._motorcycle.get_info(), "This Ninja 400 is made by Kawasaki in 2023.")

if __name__ == '__main__':
    unittest.main()