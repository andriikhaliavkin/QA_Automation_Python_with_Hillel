import pytest
import Company
import Employee



def test_get_info():
    google = Company.Company("Google", "Technology", 1998, "Mountain View, California", 160_000_000_000.0, 120_000)
    expected_info = "Google is a Technology company founded in 1998. Its headquarter is located in Mountain View, California and it has an annual revenue of 160000000000.0 and 120000 employees."
    assert google.get_info() == expected_info


def test_update_revenue():
    google = Company.Company("Google", "Technology", 1998, "Mountain View, California", 160_000_000_000, 120_000)
    google.update_revenue(165_000_000_000)
    assert google.revenue == 165_000_000_000


def test_add_employees():
    google = Company.Company("Google", "Technology", 1998, "Mountain View, California", 160_000_000_000, 120_000)
    google.add_employees(5000)
    assert google.employees == 125_000

def test_employee_info():
    e = Employee.Employee("John Snow", "Crown", 100_500, 10)
    info = e.get_info()
    assert info == "John Snow is a Crown with 10 years of experience and a salary of 100500."

def test_increase_salary():
    e = Employee.Employee("John Snow", "Crown", 100_500, 10)
    e.increase_salary(10)
    assert e.salary == 110_550.00000000001
