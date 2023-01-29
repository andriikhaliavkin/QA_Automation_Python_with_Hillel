import pytest
import library

@pytest.mark.parametrize("words, expected", [
    (["Jeff", "Alex", "Jonathan"], ["JEFF", "ALEX", "JONATHAN"]),
    (["Richelle", "Anna"], ["RICHELLE", "ANNA"]),
    (["lowercase", "words"], ["LOWERCASE", "WORDS"]),
    ([], []),
])
def test_uppercase_words(words, expected):
    result = library.uppercase_words(words)
    assert result == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], [1.000, 4.000, 9.000, 16.000]),
    ([0.123, 0.456, 0.789], [0.015, 0.208, 0.623]),
    ([-1, -2, -3], [1.000, 4.000, 9.000])
])
def test_square_and_round(numbers, expected):
    result = library.square_and_round(numbers)
    assert result == expected


@pytest.mark.parametrize("keys, values, expected_output", [
    (['a', 'b', 'c'], [1, 2, 3], {'a': 1, 'b': 2, 'c': 3}),
    (['x', 'y'], [10, 20], {'x': 10, 'y': 20}),
    (['p', 'q', 'r'], [100, 200, 300], {'p': 100, 'q': 200, 'r': 300})
])
def test_zip_lists_to_dict(keys, values, expected_output):
    assert library.zip_lists_to_dict(keys, values) == expected_output


@pytest.mark.parametrize("strings,length,expected", [
    (["Jeff", "Alex", "Jonathan", "Richelle", "Anna"], 5, ["Jeff", "Alex", "Anna"]),
    (["python", "java", "javascript"], 7, ["python", "java"]),
    (["hello", "world", "test"], 5, ["test"]),
    ([], 5, []),
    (["a", "bb", "ccc"], 1, []),
])
def test_filter_strings_by_length(strings, length, expected):
    result = library.filter_strings_by_length(strings, length)
    assert result == expected