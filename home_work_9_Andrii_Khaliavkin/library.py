def uppercase_words(words: list) -> list:
    return list(map(str.upper, words))


# uppercase_words = lambda words: list(map(str.upper, words))


def square_and_round(numbers: list) -> list:
    return list(map(lambda x: round(x ** 2, 3), numbers))


# square_and_round = lambda numbers: list(map(lambda x: round(x**2, 3), numbers))


def zip_lists_to_dict(keys: list, values: list) -> dict:
    return dict(zip(keys, values))


# zip_lists_to_dict = lambda keys, values: dict(zip(keys, values))


