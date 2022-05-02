from functools import reduce

from typing import Iterable


pepe = [1, 2, 3, 4]


def multiplicar_reduce(numeros: Iterable[float]) -> float:
    """CHALLENGE OPCIONAL - Re-escribir utilizando reduce.
    Referencia: https://docs.python.org/3.8/library/functools.html#functools.reduce
    """
    pass # Completar
    return reduce(lambda x: x * x, numeros)

multiplicar_reduce(pepe)