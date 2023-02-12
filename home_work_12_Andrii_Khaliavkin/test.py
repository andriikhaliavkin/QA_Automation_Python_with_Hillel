import pytest
import main


def test_car_initialization():
    car = main.Car("Toyota", "Camry", 2020, 20000)
    assert car.make == "Toyota"
    assert car.model == "Camry"
    assert car.year == 2020
    assert car.miles == 20000

def test_drive_method():
    car = main.Car("Toyota", "Camry", 2020, 20000)
    car.drive(100)
    assert car.miles == 20100

def test_get_info_method():
    car = main.Car("Toyota", "Camry", 2020, 20000)
    assert car.get_info() == "Toyota Camry (2020) with 20000 miles"