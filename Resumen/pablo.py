"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, name: str) -> None:
        print('se creo el articulo ' + name)
        self.name = name

    def __str__(self) -> str:
        return self.name

    # NO MODIFICAR - FIN

    # Completar


# NO MODIFICAR - INICIO
class ShoppingCart:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    def __str__(self) -> str:
        dato = '['
        for x in self.articles:
            dato = dato + str(x)

        dato = dato + ']'
        return dato
    

    # NO MODIFICAR - FIN

    # Completar


# NO MODIFICAR - INICIO

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

print(str(ShoppingCart().add(manzana).add(pera)))
# Test de conversión a String
#assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"