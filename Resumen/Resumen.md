
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


# MODULOS Y PAQUETES
## Modulo 
- Los modulos son objetos
- archivo en python (py, pyd)

## Paquete
- carpeta que contiene otros paquetes o modulos

Todos los paquetes son modulos pero no todos los modulos son paquetes, es decir, los paquetes son un tipo especial de modulos.


# Clases

## atributos y metodos
- atributos -> variables
- metodos -> funciones

## Ejmplo muy bueno para entender:
- valor de instancia, puntero ...


class Galleta:
    b=10
    
una_galleta = Galleta()
una_galleta.sabor = "Salado"
una_galleta.color = "Marrón"
una_galleta.b=20 --> este valor de b esta atado a esta instancia y por mas que camie el valor de la clase. en esta instancia va a seguir siendo 20

print("El sabor de esta galleta es",una_galleta.sabor)
print(una_galleta.b)
c = Galleta()
print("c.b ",c.b)
Galleta.b=50 --> aunque pase a ser 50, en b seguira siendo 20
print("c.b ",c.b)
print("una_galleta ",una_galleta.b)
a = Galleta()
 

## Metodos CONSTRUCTOR Y DESTRUCTOR

- Self sirve para hacer referencia a los metodos y atibutos base de una clase dentro de sus propios metodos

class Pelicula:
    # Constructor de clase (al crear la instancia)
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
        
    # Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("Se está borrando la película", self.titulo)
        
p = Pelicula("El Padrino",175,1972)

## Metodos y variables de clase

### Los metodos de clase se declaran debajo de esto:
#### @classmethod y en vez de self va cls 
def metodo_de_clase(cls)

### Las variables de clase de declaran fuera de las funciones
Pero es una cuestion de nomenclatura
porque si desde una instancia modificas la variable de clase
lo que sucede es que Se crea una variables para esa instancia
con el mismo nombre que la variables de clase y la variable
de clase no se modifica.


## dataclass
Te permite definir que variables van en el constructor
soloamente definiendo las variables para esa clase

## Properties
https://docs.python.org/3/library/functions.html#property

Encapsula los metodos de instancia que cambian valores en las vriables de instancias