import library

def test_is_hot_today():
    assert library.is_hot_today(30) == "Hot"
    assert library.is_hot_today(20) == "Cold"
    assert library.is_hot_today(35) == "Hot"
    assert library.is_hot_today(-5) == "Cold"
    assert library.is_hot_today(25) == "Cold"
    assert library.is_hot_today(26) == "Hot"
    assert library.is_hot_today() == "Hot" # test with default value
    assert library.is_hot_today("not a number") == "приймаються тільки числа"

test_is_hot_today()

def test_atm():
    assert library.atm(100) == ["100 гривень", "0 копійок"]
    assert library.atm(100.50) == ["100 гривень", "50 копійок"]
    assert library.atm(-100) == "вартість не може бути від'ємною"
    assert library.atm("a hundred") == "приймаються тільки числа"

test_atm()

def test_banknotes():
    assert library.banknotes(1) == "1 гривня"
    assert library.banknotes(5) == "5 гривень"
    assert library.banknotes(11) == "11 гривень"
    assert library.banknotes(12) == "12 гривень"
    assert library.banknotes(21) == "21 гривня"
    assert library.banknotes(22) == "22 гривні"
    assert library.banknotes(25) == "25 гривень"
    assert library.banknotes(-1) == "вартість не може бути від'ємною"
    assert library.banknotes("abc") == "приймаються тільки числа"

test_banknotes()


def test_coins():
    assert library.coins(5) == "5 копійок"
    assert library.coins(12) == "12 копійок"
    assert library.coins(1) == "1 копійка"
    assert library.coins(2) == "2 копійки"
    assert library.coins(-5) == "вартість не може бути від'ємною"
    assert library.coins(5.5) == "5 копійок"
    assert library.coins("five") == "приймаються тільки числа"


test_coins()