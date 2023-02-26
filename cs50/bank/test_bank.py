from bank import value


def test_value_Hello():
    assert value("Hello") == "$0"
    assert value("Hello, world") == "$0"


def test_value_h():
    assert value("hi boys") == "$20"
    assert value("Hell") == "$20"
    assert value("How you doing?") == "$20"


def test_value_else():
    assert value(" boys") == "$100"
    assert value("What's going on?") == "$100"
    assert value("ell") == "$100"
