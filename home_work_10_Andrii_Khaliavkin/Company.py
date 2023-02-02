# Створіть клас з описом будь-якої компанії. Наприклад Hillel, Epam, Google.
# Намагайтесь максимально повно описати класи на предмет полів і методів.
# Додайте анотації до всіх методів. До кожного метода обов'язково треба
# додати док стрінгу з описом метода і анотації.


class Company:
    """A class representing a company."""

    def __init__(self, name: str, industry: str, founded_year: int, headquarter: str, revenue: float, employees: int):
        """Initialize the company with the following attributes:
        Args:
        name (str): The name of the company.
        industry (str): The industry the company operates in.
        founded_year (int): The year the company was founded.
        headquarter (str): The location of the company's headquarter.
        revenue (float): The annual revenue of the company.
        employees (int): The number of employees in the company.
        """
        self.name = name
        self.industry = industry
        self.founded_year = founded_year
        self.headquarter = headquarter
        self.revenue = revenue
        self.employees = employees

    def get_info(self) -> str:
        """Return a string with information about the company.
        Returns:
            str: A string with information about the company, including name, industry, founded year, headquarter,
        revenue, and number of employees.
        """
        return f"{self.name} is a {self.industry} company founded in {self.founded_year}. Its headquarter is located in {self.headquarter} and it has an annual revenue of {self.revenue} and {self.employees} employees."

    def update_revenue(self, new_revenue: float) -> None:
        """Update the company's annual revenue.
        Args:
            new_revenue (float): The new revenue of the company.
        Returns:
            None
        """
        self.revenue = new_revenue

    def add_employees(self, additional_employees: int) -> None:
        """Add employees to the company.
        Args:
            additional_employees (int): The number of employees to add to the company.
        Returns:
            None
        """
        self.employees += additional_employees