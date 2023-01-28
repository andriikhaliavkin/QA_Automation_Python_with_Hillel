# написати функцію, яка отримує ціле число і повертає слово "копійка" у вірній формі: 1 -- копійка, 2 -- копійки, 25 -- копійок


def coins(coins_quantity):
    """
        This function takes a number as an input and returns a string with the correct grammatical form of the word "копійка".
        If the input is not a positive integer, the function will return an error message.
        :param coins_quantity: the number of coins
        :type coins_quantity: int
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
        print("приймаються тільки цілі числа без спец. символів")


# написати функцію, яка отримує ціле число і повертає слово "гривня" у вірній формі: 1 -- гривня, 2 -- гривні, 25 -- гривень
def banknotes(banknotes_quantity):
    """
        This function takes a number as an input and returns a string with the correct grammatical form of the word "гривня".
        If the input is not a positive integer, the function will return an error message.
        :param banknotes_quantity: the number of banknotes
        :type banknotes_quantity: int
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
        print("приймаються тільки цілі числа без спец. символів")



