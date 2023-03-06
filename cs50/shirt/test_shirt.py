from shirt import *


def test_incorrect_input():
    assert not incorrect_input("hello.png")
    assert not incorrect_input("o.jpg")
    assert not incorrect_input("o.jpeg")
    assert incorrect_input("o.peg")

def test_incorrect_output():
    assert not incorrect_output("o.png", "h.png")
    assert incorrect_output("o.jpg", "h.png")
