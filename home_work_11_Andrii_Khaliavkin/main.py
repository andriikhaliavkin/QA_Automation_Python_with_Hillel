# Потрібно описати будь-який транспортний засіб або гаджет(на вибір) , з кількома рівнями абстракції,
# використовуючи ті принципи ООП, що ми розглядали: наслідування абстракцію і приховування даних.

class Gadget:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Smartphone(Gadget):
    def __init__(self, brand, model, price, operating_system, screen_size, camera_resolution):
        Gadget.__init__(self, brand, model, price)
        self.operating_system = operating_system
        self.screen_size = screen_size
        self.camera_resolution = camera_resolution


class Smartphone(Gadget):
    def __init__(self, brand, model, price, operating_system, screen_size, camera_resolution):
        Gadget.__init__(self, brand, model, price)
        self.__operating_system = operating_system
        self.__screen_size = screen_size
        self.__camera_resolution = camera_resolution

    def get_operating_system(self) -> str:
        """
        Returns:
            str: Operating system
        """
        return self.__operating_system

    def get_screen_size(self) -> float:
        """
        Returns:
            float: The screen size
        """
        return self.__screen_size

    def get_camera_resolution(self) -> int:
        """
        Returns:
            int: camera's resolution
        """
        return self.__camera_resolution


samsung_galaxy = Smartphone("Samsung", "Galaxy S21", 1000, "Android", 6.2, 64)
