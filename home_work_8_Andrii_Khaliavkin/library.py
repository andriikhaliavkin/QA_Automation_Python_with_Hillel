import math


# написати функцію, яка отримує ціле число і повертає слово "копійка" у вірній формі: 1 -- копійка, 2 -- копійки, 25 -- копійок
def coins(coins_quantity):
    """
        This function takes a number as an input and returns a string with the correct grammatical form of the word "копійка".
        If the input is not a positive integer, the function will return an error message.
        :param coins_quantity: the number of coins
        :type coins_quantity: int / float
        :return: string with the grammatically correct form of "копійка"
        :rtype: str
    """
    try:
        coins_quantity = int(coins_quantity)
        if coins_quantity < 0:
            print("кількість копійок не може бути від'ємною")
        else:
            if coins_quantity % 10 == 1 and coins_quantity != 11:
                return f"{coins_quantity} копійка"
            elif coins_quantity % 10 in (2, 3, 4) and coins_quantity not in (12, 13, 14):
                return f"{coins_quantity} копійки"
            else:
                return f"{coins_quantity} копійок"
    except ValueError:
        print("приймаються тільки числа")


# написати функцію, яка отримує ціле число і повертає слово "гривня" у вірній формі: 1 -- гривня, 2 -- гривні, 25 -- гривень
def banknotes(banknotes_quantity):
    """
        This function takes a number as an input and returns a string with the correct grammatical form of the word "гривня".
        If the input is not a positive integer, the function will return an error message.
        :param banknotes_quantity: the number of banknotes
        :type banknotes_quantity: int / float
        :return: string with the grammatically correct form of "гривня"
        :rtype: str
    """
    try:
        banknotes_quantity = int(banknotes_quantity)
        if banknotes_quantity < 0:
            print("кількість гривень не може бути від'ємною")
        else:
            if banknotes_quantity % 10 == 1 and banknotes_quantity != 11:
                return f"{banknotes_quantity} гривня"
            elif banknotes_quantity % 10 in (2, 3, 4) and banknotes_quantity not in (12, 13, 14):
                return f"{banknotes_quantity} гривні"
            else:
                return f"{banknotes_quantity} гривень"
    except ValueError:
        print("приймаються тільки числа")


# написати функцію, яка приймає число і повертає список, в якому перший елемент - стрічка з цілою частиною числа + слово 'гривня'
# у вірному відмінку, другий елемент - стрічка з мантісою (значення після коми), + слово 'копійка' у вірній формі. \
# наприклад - 1 -- ['1 гривня', "0 копійок"]; 10.1 -- ['10 гривень', "10 копійок"]; 2.01 -- ['2 гривні', "1 копійка"].
# в даній функції для створення форм слів гривня та копійка використати результат роботи функцій, описаних вище.
# Зауваження - якщо буде передано число з дрібною частиною більш ніж 2 знаки, то вони не мають оброблятися
# (логіку, що робити з 125.339 залишаю на вас - чи округляйте, чи відкидайте - і це рішення пропишіть в докстрінгі)

def atm(money):
    """
    This function takes a number as an input and returns a list with integer and fractional parts of it with correct
    grammatical form of the words "гривня" and "копійка". Fractional parts are rounded to 2 decimals after coma.
    :param money: the number of money
    :type money: int / float
    :return: splitted number on its integer and fractional parts with correct grammatical form of the words "гривня" and "копійка"
    :rtype: list
    """
    try:
        money = round(float(money), 2)
        if money < 0:
            print("вартість не може бути від'ємною")
        else:
            kopijky, hrywni = math.modf(money)
            kopijky = round(kopijky * 100, 0)
            bank_account = [banknotes(hrywni), coins(kopijky)]
            return bank_account
    except ValueError:
        print("приймаються тільки числа")


# напишіть функцію is_hot_today, яка отримує параметр температури (число, за замовчуванням 30), і в залежності від величини
# повідомляє, чи сьогодні жарко, чи холодно (більше 25 - жарко, інакше холодно). перевірку на -155555555555 градусів
# чи +555555555555 не проводимо, просто відштовхуємося від отриманого значення. подумайте, який тип даних має повертати функція

def is_hot_today(temperature=30):
    """
        This function takes in an optional parameter 'temperature' which is a number representing the temperature.
        It checks if the temperature is greater than 25, if yes, returns "Hot", otherwise returns "Cold".
        The default value for temperature is 30.
        In case of invalid input (not a number) it will throw ValueError and print "приймаються тільки числа"
        :param temperature: number which represents a temperature
        :type temperature: int / float
        :return: whether condition cold or hot
        :rtype: str
    """
    try:
        temperature = int(temperature)
        if temperature > 25:
            return "Hot"
        else:
            return "Cold"
    except ValueError:
        print("приймаються тільки числа")

# створіть функцію, яка отримує від користувача число і повертає його як число. проте!!! якщо користувач ввів не вірні дані,
# які не можна конвертувати в число ("шість"), заставте користувача ввести валідні дані (цикли вам в допомогу).
# результатом в будь-якому випадку має бути число. зауважте - функція має прийняти один не обовязковий стрічковий
# аргумент - месседж, за замовчуванням - "Введіть число"

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

