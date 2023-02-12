# Опишіть будь-який об'єкт, який має методи, що змінюють його стани.


class Car:
    """Class describes behavior of object Car"""

    def __init__(self, make: str, model: str, year: int, miles: int):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__miles = miles

    @property
    def make(self) -> str:
        return self.__make

    @property
    def model(self) -> str:
        return self.__model

    @property
    def year(self) -> int:
        return self.__year

    @property
    def miles(self) -> int:
        return self.__miles

    def drive(self, distance: int) -> None:
        """
        Increase the miles driven by the car

        Args:
            distance (int): The distance driven by the car

        """
        self.__miles += distance

    def get_info(self) -> str:
        """
        Get information about the car

        Returns:
            info (str): Information about the car
        """
        info = f"{self.__make} {self.__model} ({self.__year}) with {self.__miles} miles"
        return info


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 20000)
    print(car.make)
    print(car.model)
    print(car.year)
    print(car.miles)

    car.drive(100)
    print(car.miles)

    print(car.get_info())
