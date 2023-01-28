import library
import pytest


@pytest.mark.parametrize("test_input, expected", [(30, "Hot"), (20, "Cold"), (35, "Hot"), (-5, "Cold")])
def test_check_the_weather(test_input, expected):
    assert library.check_the_weather(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [(100, ["100 гривень", "0 копійок"]), (100.50, ["100 гривень", "50 копійок"])])
def test_atm(test_input, expected):
    assert library.atm(test_input) == expected
#

#     def test_banknotes(self):
#         assert library.banknotes(1) == "1 гривня"
#         assert library.banknotes(5) == "5 гривень"
#         assert library.banknotes(11) == "11 гривень"
#         assert library.banknotes(12) == "12 гривень"
#         assert library.banknotes(21) == "21 гривня"
#         assert library.banknotes(22) == "22 гривні"
#         assert library.banknotes(25) == "25 гривень"
#         assert library.banknotes(-1) == "вартість не може бути від'ємною"
#         assert library.banknotes("abc") == "приймаються тільки числа"
#
#     def test_coins(self):
#         assert library.coins(5) == "5 копійок"
#         assert library.coins(12) == "12 копійок"
#         assert library.coins(1) == "1 копійка"
#         assert library.coins(2) == "2 копійки"
#         assert library.coins(-5) == "вартість не може бути від'ємною"
#         assert library.coins(5.5) == "5 копійок"
#         assert library.coins("five") == "приймаються тільки числа"
#
#
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAll)
# unittest.TextTestRunner().run(suite)
