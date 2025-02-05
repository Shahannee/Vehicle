import unittest
import vehicle as ve

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

    def test_create_vehicle_error_handling(self):
        """Verifying error handling when unexpected values are given to the method."""
        with self.assertRaisesRegex(ve.VehicleTypeError, "Invalid vehicle type. Please choose 'CAR' or 'MOTORCYCLE'."):
            ve.create_vehicle("car", 50, 2024, "Tesla", "Model S")

        with self.assertRaisesRegex(ValueError, "The fuel capacity must be a positive number."):
            ve.create_vehicle(ve.VehicleType.CAR, -5, 2024, "Tesla", "Model S")


    def test_drive_car(self):
        expected_output = "Driving a car."
        self.assertEqual(self._car.drive(), expected_output)

    def test_drive_motorcycle(self):
        expected_output = "Driving a motorcycle."
        self.assertEqual(self._motorcycle.drive(), expected_output)

    def test_fuel_method_for_car(self):
        self.assertEqual(self._car.get_fuel_capacity() * ve.FuelPercent.FULL.value, 50)
        self.assertEqual(self._car.get_fuel_capacity() * ve.FuelPercent.THREE_QUARTERS.value, 37.5)
        self.assertEqual(self._car.get_fuel_capacity() * ve.FuelPercent.HALF.value, 25)
        self.assertEqual(self._car.get_fuel_capacity() * ve.FuelPercent.ONE_QUARTER.value, 12.5)

    def test_fuel_method_for_car_error_handling(self):
        """Verifying error handling when unexpected value is given to the method."""
        with self.assertRaisesRegex(ValueError, "Invalid fuel percentage. "
                                                "Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL."):
            self._car.fuel(50)


    def test_fuel_method_for_motorcycle(self):
        self.assertEqual(self._motorcycle.get_fuel_capacity() * ve.FuelPercent.FULL.value, 15)
        self.assertEqual(self._motorcycle.get_fuel_capacity() * ve.FuelPercent.THREE_QUARTERS.value, 11.25)
        self.assertEqual(self._motorcycle.get_fuel_capacity() * ve.FuelPercent.HALF.value, 7.5)
        self.assertEqual(self._motorcycle.get_fuel_capacity() * ve.FuelPercent.ONE_QUARTER.value, 3.75)

    def test_fuel_method_for_motorcycle_error_handling(self):
        """ Verifying error handling when unexpected value is given to the method."""
        with self.assertRaisesRegex(ValueError, f"15 is invalid fuel percentage. "
                                                "Please choose from ONE_QUARTER, HALF, THREE_QUARTERS, or FULL."):
            self._motorcycle.fuel(15)

    def test_get_info_car(self):
        self.assertEqual(self._car.get_info(), "This Corolla is made by Toyota in 2024.")

    def test_get_info_motorcycle(self):
        self.assertEqual(self._motorcycle.get_info(), "This Ninja 400 is made by Kawasaki in 2023.")

if __name__ == '__main__':
    unittest.main()