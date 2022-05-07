
# TEORIA DEL ARCHIVO 


# Variables y sus ID's
- Al asignarles un valor, python les asigna un ID
- si le cambias el valor a la variable, cambia su ID
- A = 4 -->  priunt(id(A)) --> tiene un ID
- si hago B = A , ambas tienen el mismo ID


# LISTAS, SETS, IF, WHILE, FOR
- Una forma de verlo es que todo lo mutable se pasa por REFERENCIA
-   para que no se pase por referencia hay que usar deepcopy
    a = [1,3,4,5]
    b = deepcopy(a)
    Si cambio el valor de b ahora no afecta a "a" porque no se relacionan por referencia

## TUPLAS
-  Las TUPLAS NO SON MUTABLES

## SETS
- tipos de datos iterables --> s = set([1,5,6]) o sino s = {1,3,4,5}
- los set son mutables... para hacerlos inmutables hay que usar fronzenset([1,4,5])

## BOOLEANOS
- bool es un derivado de int
- 1 es true
- 0 es false

## FOR Y WHILE
- Repasar todos los tipos de while y for

# COMPRENSION DE LISTAS
- Provee una manera concisa de crear listas
- Consiste en pasar de esto:
    - `squares = list(map(lambda x: x**2, range(10)))`
- A esto:
    - `squares = [x**2 for x in range(10)]`
- Siempre empieza con corchetes, una expresion seguida de un for y despues cero o mas for o if.


# Funciones y Clases
- Las funciones pueden devolver mas de un valor



# MODULOS Y PAQUETES
## Modulo 
- Los modulos son objetos
- archivo en python (py, pyd)

## Paquete
- carpeta que contiene otros paquetes o modulos

Todos los paquetes son modulos pero no todos los modulos son paquetes, es decir, los paquetes son un tipo especial de modulos.
