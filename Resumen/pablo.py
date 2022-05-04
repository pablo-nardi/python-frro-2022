from functools import reduce

from typing import Iterable


def func(num, num2):
    num = num + 1
    num2 = num2 + 2
    return num, num2

x, y = func(2,2)
print(x, y)