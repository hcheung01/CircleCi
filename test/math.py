import pytest
from src.math import Math as Math2

@pytest.fixture
def a():
    return 100

@pytest.fixture
def b():
    return 1

math = Math2()

def test_add(a, b):
    total = math.add(a, b)
    assert total != 100
    assert total == 101

def test_subtract(a, b):
    total = math.subtract(a, b)
    assert total == 99

def test_multiply(a, b):
    total = math.multiply(a, b)
    assert b == 1
    assert a == total

def test_divide(a, b):
    total = math.divide(a, b)
    assert b == 1
    assert a == total



