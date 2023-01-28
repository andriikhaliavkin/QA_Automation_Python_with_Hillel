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