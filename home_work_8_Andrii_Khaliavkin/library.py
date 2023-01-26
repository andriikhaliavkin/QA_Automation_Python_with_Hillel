# написати функцію, яка отримує ціле число і повертає слово "копійка" у вірній формі: 1 -- копійка, 2 -- копійки, 25 -- копійок


def coins(user_input):
    """     """
    try:
        user_input = int(user_input)
        if user_input < 0:
            print("кількість копійок не може бути від'ємною")
        else:
            if user_input % 10 == 1 and user_input != 11:
                return f"{user_input} копійка"
            elif user_input % 10 in (2, 3, 4) and user_input not in (12, 13, 14):
                return f"{user_input} копійки"
            else:
                return f"{user_input} копійок"
    except ValueError:
        print("приймаються тільки цілі числа без спец. символів")







print(coins(-1))
print(coins(2))
print(coins('d'))