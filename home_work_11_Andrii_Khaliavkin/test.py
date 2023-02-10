import pytest
import main

def test_get_operating_system():
    samsung_galaxy = main.Smartphone("Samsung", "Galaxy S21", 1000, "Android", 6.2, 64)
    assert samsung_galaxy.get_operating_system() == "Android"

def test_get_screen_size():
    samsung_galaxy = main.Smartphone("Samsung", "Galaxy S21", 1000, "Android", 6.2, 64)
    assert samsung_galaxy.get_screen_size() == 6.2

def test_get_camera_resolution():
    samsung_galaxy = main.Smartphone("Samsung", "Galaxy S21", 1000, "Android", 6.2, 64)
    assert samsung_galaxy.get_camera_resolution() == 64