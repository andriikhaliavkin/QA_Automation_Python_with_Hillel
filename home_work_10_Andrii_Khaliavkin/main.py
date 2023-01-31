import Company
import Employee

google = Company.Company("Google", "Technology", 1998, "Mountain View, California", 160_000_000_000.0, 120_000)
print(google.get_info())

John_Snow = Employee.Employee("John Snow", "Black Crown", 100500.0, 20)
print(John_Snow.get_info())
