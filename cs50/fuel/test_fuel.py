from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("0/3") == 0
    assert convert("999/1000") == 100


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(9) == "9%"
