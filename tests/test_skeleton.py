import pytest

from latex_escape.skeleton import fib

__author__ = "Carli* Freudenberg"
__copyright__ = "Carli* Freudenberg"
__license__ = "MIT"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
