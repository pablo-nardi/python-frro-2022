"""Propiedades"""


class Auto:
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    # Completar
    def __init__(self, marca, precio: float) -> None:
        self._marca = marca
        self._precio = precio

    def _get_marca(self):
        return self._marca

    def _get_precio(self):
        return round(self._precio)

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
auto = Auto("Ford", 12875.456)
print(auto.nombre)
print(auto.precio)

assert auto.nombre == "Ford"
assert auto.precio == 12875.46
auto.precio = 13874.349
assert auto.precio == 13874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
