import pytest
from calculator import add, subtract, division, double

def test_add():
    assert add(1, 2) == 3
    assert add(10, 3) == 13

def test_subtract():
    assert subtract(-5, -2) == -3
    # assert subtract(20.1, 5) == 15.1

def test_division():
    assert division(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)

def test_double_user_input(monkeypatch):
    inputs = iter(['10', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert double() == 20
    assert double() == 8
