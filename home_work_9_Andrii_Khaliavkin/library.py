
def uppercase_words(words: list) -> list:
    return list(map(str.upper, words))


# uppercase_words = lambda words: list(map(str.upper, words))


def square_and_round(numbers):
    return list(map(lambda x: round(x**2, 3), numbers))

# square_and_round = lambda numbers: list(map(lambda x: round(x**2, 3), numbers))

