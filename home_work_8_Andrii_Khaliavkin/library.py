import math


def transcript_the_number_of_coins(coins_quantity: float) -> str:
    """
    """
    coins_quantity = abs(int(coins_quantity))
    if not isinstance(coins_quantity, int):
        raise TypeError("coins_quantity must be an int")

    if coins_quantity % 10 == 1 and coins_quantity != 11:
        return f"{coins_quantity} копійка"
    elif coins_quantity % 10 in (2, 3, 4) and coins_quantity not in (12, 13, 14):
        return f"{coins_quantity} копійки"
    else:
        return f"{coins_quantity} копійок"



def transcript_the_number_of_banknotes(banknotes_quantity: float) -> str:
    """
    """
    banknotes_quantity = abs(int(banknotes_quantity))
    if not isinstance(banknotes_quantity, int):
        raise TypeError("banknotes_quantity must be an int")

    if banknotes_quantity % 10 == 1 and banknotes_quantity != 11:
        return f"{banknotes_quantity} гривня"
    elif banknotes_quantity % 10 in (2, 3, 4) and banknotes_quantity not in (12, 13, 14):
        return f"{banknotes_quantity} гривні"
    else:
        return f"{banknotes_quantity} гривень"


def transcript_the_amount_of_money(money: float) -> list:
    """
    """
    money = abs(round(float(money), 2))
    if not isinstance(money, float):
        raise TypeError("money must be float")

    hrywni, kopijky = divmod(money,1)
    kopijky = round(kopijky * 100, 0)
    bank_account = [transcript_the_number_of_banknotes(hrywni), transcript_the_number_of_coins(kopijky)]

    return bank_account


def check_the_weather(temperature: int) -> str:
    """
    """
    temperature = int(temperature)
    if not isinstance(temperature, int):
        raise TypeError("temperature must be an int")

    if temperature > 25:
        return "Hot"
    else:
        return "Cold"


def receive_user_input():
    """
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
