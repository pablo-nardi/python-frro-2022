"""Propiedades"""


class Auto:
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    # Completar
    def __init__(self, marca: str, precio: float) -> None:
        self._marca = marca.capitalize()
        self._precio = precio

    def _get_marca(self):
        return self._marca

    def _get_precio(self):
        return round(self._precio, 2)

    def _set_precio(self, precio):
        self._precio = precio

    nombre = property(
        fget= _get_marca
    )

    precio = property(
        fget= _get_precio,
        fset= _set_precio
    )


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    """Re-Escribir utilizando DataClasses"""

    # Completar
    _marca: str
    _precio: float

    def _get_marca(self):
        return self._marca.capitalize()

    def _get_precio(self):
        return round(self._precio,2)

    def _set_precio(self, precio):
        self._precio = precio

    marca = property(
        fget= _get_marca
    )

    precio = property(
        fget= _get_precio,
        fset= _set_precio
    )

# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.marca == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35


try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
