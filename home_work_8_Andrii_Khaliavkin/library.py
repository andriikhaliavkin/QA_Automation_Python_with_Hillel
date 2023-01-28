import math


def transcript_the_number_of_coins(coins_quantity: int) -> str:
    """
    """
    try:
        coins_quantity = abs(int(coins_quantity))
        if coins_quantity % 10 == 1 and coins_quantity != 11:
            return f"{coins_quantity} копійка"
        elif coins_quantity % 10 in (2, 3, 4) and coins_quantity not in (12, 13, 14):
            return f"{coins_quantity} копійки"
        else:
            return f"{coins_quantity} копійок"
    except ValueError:
        return f"приймаються тільки числа"


def transcript_the_number_of_banknotes(banknotes_quantity: int) -> str:
    """
    """
    try:
        banknotes_quantity = abs(int(banknotes_quantity))
        if banknotes_quantity % 10 == 1 and banknotes_quantity != 11:
            return f"{banknotes_quantity} гривня"
        elif banknotes_quantity % 10 in (2, 3, 4) and banknotes_quantity not in (12, 13, 14):
            return f"{banknotes_quantity} гривні"
        else:
            return f"{banknotes_quantity} гривень"
    except ValueError:
        return f"приймаються тільки числа"


def transcript_the_amount_of_money(money: float) -> list:
    """
    """
    try:
        money = abs(round(float(money), 2))
        kopijky, hrywni = math.modf(money)
        kopijky = round(kopijky * 100, 0)
        bank_account = [transcript_the_number_of_banknotes(hrywni), transcript_the_number_of_coins(kopijky)]
        return bank_account
    except ValueError:
        return f"приймаються тільки числа"


def check_the_weather(temperature: int) -> str:
    """
    """
    temperature = int(temperature)
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
