def transcript_the_number_of_coins(coins_quantity: float) -> str:
    """
        receives number and returns text transcription amount of coins (str)
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
        if not isinstance(coins_quantity, int):
            raise ValueError("coins_quantity must be an int")



def transcript_the_number_of_banknotes(banknotes_quantity: float) -> str:
    """
        receives number and returns text transcription amount of banknotes (str)
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
        if not isinstance(banknotes_quantity, int):
            raise ValueError("banknotes_quantity must be an int")


def transcript_the_amount_of_money(money: float) -> list:
    """
        receives number and returns text transcript amount of banknotes and coins (list)
    """
    try:
        money = abs(round(float(money), 2))
        hrywni, kopijky = divmod(money,1)
        kopijky = round(kopijky * 100, 0)
        bank_account = [transcript_the_number_of_banknotes(hrywni), transcript_the_number_of_coins(kopijky)]
        return bank_account
    except ValueError:
        if not isinstance(money, float):
            raise ValueError("money must be float")

def check_the_weather(temperature: int) -> str:
    """
    """
    try:
        temperature = int(temperature)
        if temperature > 25:
            return "Hot"
        else:
            return "Cold"
    except ValueError:
        if not isinstance(temperature, int):
            raise ValueError("temperature must be an int")

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
