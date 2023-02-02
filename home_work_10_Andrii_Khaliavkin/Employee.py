# Створіть клас з описом будь-якого працівника(Типу універсальний). Employee.
# Намагайтесь максимально повно описати класи на предмет полів і методів.
# Додайте анотації до всіх методів. До кожного метода обов'язково треба
# додати док стрінгу з описом метода і анотації.


class Employee:
    """
    Class representing an employee.
    """

    def __init__(self, name: str, position: str, salary: float, experience: int):
        """
        Initialize an Employee instance.

        Args:
            name (str): Name of the employee.
            position (str): Position of the employee.
            salary (float): Salary of the employee.
            experience (int): Years of experience of the employee.
        """
        self.name = name
        self.position = position
        self.salary = salary
        self.experience = experience

    def get_info(self) -> str:
        """
        Return a string with information about the employee.

        Returns:
            str: A string with information about the employee.
        """
        return f"{self.name} is a {self.position} with {self.experience} years of experience and a salary of {self.salary}."

    def increase_salary(self, percent: float) -> None:
        """
        Increase the salary of the employee by a certain percentage.

        Args:
            percent (float): The percentage by which the salary will be increased.
        Returns:
            None
        """
        self.salary *= 1 + percent / 100

    def change_position(self, new_position: str) -> None:
        """
        Change the position of the employee.

        Args:
            new_position (str): The new position of the employee.

        Returns:
            None
        """
        self.position = new_position

    def increase_experience(self) -> None:
        """
        Increase the experience of the employee by one year.

        Returns:
            None
        """
        self.experience += 1
