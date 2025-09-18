import pytest

from src.math_utils import multiply




def test_basic_math():
    assert  2 + 2 == 4


@pytest.mark.parametrize(
    "num1, num2, result",
    [
    (2, 2, 4),
    (3, 5, 15),
    (-3, 5, -15),
    (-3, -5, 15)
    ]
)
def test_multiply(num1, num2, result):
    assert multiply(num1, num2)== result
    "функция загрушена не правильно"

