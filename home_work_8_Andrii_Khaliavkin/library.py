# написати функцію, яка отримує ціле число і повертає слово "копійка" у вірній формі: 1 -- копійка, 2 -- копійки, 25 -- копійок


def coins(number):
    """     """
    try:
        number = int(number)
        if number < 0:
            print("кількість копійок не може бути від'ємною")
        else:
            if number % 10 == 1 and number != 11:
                return f"{number} копійка"
            elif number % 10 in (2, 3, 4) and number not in (12, 13, 14):
                return f"{number} копійки"
            else:
                return f"{number} копійок"
    except ValueError:
        print("приймаються тільки цілі числа без спец. символів")







print(coins(-1))
print(coins(2))
print(coins('d'))