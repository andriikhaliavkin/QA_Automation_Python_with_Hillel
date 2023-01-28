import math


def coins(coins_quantity):
    """
        :param coins_quantity: the number of coins
        :type coins_quantity: int / float
        :return: string with the grammatically correct form of "копійка"
        :rtype: str
    """
    try:
        coins_quantity = int(coins_quantity)
        if coins_quantity < 0:
            return f"вартість не може бути від'ємною"
        else:
            if coins_quantity % 10 == 1 and coins_quantity != 11:
                return f"{coins_quantity} копійка"
            elif coins_quantity % 10 in (2, 3, 4) and coins_quantity not in (12, 13, 14):
                return f"{coins_quantity} копійки"
            else:
                return f"{coins_quantity} копійок"
    except ValueError:
        return f"приймаються тільки числа"

def banknotes(banknotes_quantity):
    """
        :param banknotes_quantity: the number of banknotes
        :type banknotes_quantity: int / float
        :return: string with the grammatically correct form of "гривня"
        :rtype: str
    """
    try:
        banknotes_quantity = int(banknotes_quantity)
        if banknotes_quantity < 0:
            return f"вартість не може бути від'ємною"
        else:
            if banknotes_quantity % 10 == 1 and banknotes_quantity != 11:
                return f"{banknotes_quantity} гривня"
            elif banknotes_quantity % 10 in (2, 3, 4) and banknotes_quantity not in (12, 13, 14):
                return f"{banknotes_quantity} гривні"
            else:
                return f"{banknotes_quantity} гривень"
    except ValueError:
        return f"приймаються тільки числа"


def atm(money):
    """
    :param money: the number of money
    :type money: int / float
    :return: splitted number on its integer and fractional parts with correct grammatical form of the words "гривня" and "копійка"
    :rtype: list
    """
    try:
        money = round(float(money), 2)
        if money < 0:
            return f"вартість не може бути від'ємною"
        else:
            kopijky, hrywni = math.modf(money)
            kopijky = round(kopijky * 100, 0)
            bank_account = [banknotes(hrywni), coins(kopijky)]
            return bank_account
    except ValueError:
        return f"приймаються тільки числа"


def check_the_weather(temperature=30):
    """
        :param temperature: number which represents a temperature
        :type temperature: int / float
        :return: whether condition cold or hot
        :rtype: str
    """
    temperature = int(temperature)
    if temperature > 25:
        return "Hot"
    else:
        return "Cold"



def user_number_input():
    """
        This function prompts the user to input a number.
        It checks if the input is a valid number and greater than or equal to 0.
        If the input is not a valid number, it throws a ValueError and prompts the user to enter a valid number.
        If the input is less than 0, it throws an error and prompts the user to enter a number greater than or equal to 0.
        It returns the valid input number.
        :return: user's input
        :rtype: float
    """
    while True:
        try:
            user_input = float(input("Введіть число "))
            if user_input < 0:
                print("вартість не може бути від'ємною")
                continue
            return user_input
        except ValueError:
            print("приймаються тільки числа")
            continue

