
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:

    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    pass # Completar
    letras = []
    enteros = []

    for i in lista:
        if type(i) == str:
            letras.append(i)
        else:
            enteros.append(i)

    print(letras + enteros)
        

# NO MODIFICAR - INICIO
#assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
numeros_al_final_basico([3, "a", 1, "b", 10, "j"])