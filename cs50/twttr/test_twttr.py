from twttr import shorten


def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("AEioubcdaeIOU") == "bcd"
