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
            kopijky = round(kopijky*100, 0)
            bank_account = [banknotes(hrywni), coins(kopijky)]
            print(bank_account)
            return bank_account
    except ValueError:
        print("приймаються тільки числа")

