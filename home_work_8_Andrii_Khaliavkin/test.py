import library
import pytest


@pytest.mark.parametrize("test_input, expected",
                         [(1, "1 копійка"), (5, "5 копійок"), (2, "2 копійки"), (12, "12 копійок")])
def test_transcript_the_number_of_coins_with_valid_inputs(test_input, expected):
    assert library.transcript_the_number_of_coins(test_input) == expected


def test_transcript_the_number_of_coins_with_invalid_inputs():
    with pytest.raises(ValueError):
        library.transcript_the_number_of_coins("a")


@pytest.mark.parametrize("test_input, expected",
                         [(1, "1 гривня"), (5, "5 гривень"), (22, "22 гривні"), (21, "21 гривня")])
def test_transcript_the_number_of_banknotes_with_valid_inputs(test_input, expected):
    assert library.transcript_the_number_of_banknotes(test_input) == expected


def test_transcript_the_number_of_banknotes_with_invalid_inputs():
    with pytest.raises(ValueError):
        library.transcript_the_number_of_banknotes("a")


@pytest.mark.parametrize("test_input, expected",
                         [(100, ["100 гривень", "0 копійок"]), (100.50, ["100 гривень", "50 копійок"])])
def test_transcript_the_amount_of_money_with_valid_inputs(test_input, expected):
    assert library.transcript_the_amount_of_money(test_input) == expected

def test_transcript_the_amount_of_money_with_invalid_inputs():
    with pytest.raises(ValueError):
        library.transcript_the_amount_of_money("a")


@pytest.mark.parametrize("test_input, expected", [(30, "Hot"), (20, "Cold"), (35, "Hot"), (-5, "Cold")])
def test_check_the_weather_with_valid_inputs(test_input, expected):
    assert library.check_the_weather(test_input) == expected


def test_check_the_weather_with_invalid_inputs():
    with pytest.raises(ValueError):
        library.check_the_weather("a")
