from abc import ABC, abstractmethod

class Coleccion(ABC):
    @abstractmethod
    def insertarElemento(self, elemento, posicion):
        pass

    @abstractmethod
    def agregarElemento(self, elemento):
        pass

    @abstractmethod
    def mostrarElemento(self, posicion):
        pass

class MiColeccion(Coleccion):
    def __init__(self):
        self.elementos = []

    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > len(self.elementos):
            raise ValueError("La posición dada no es válida para la inserción")
        self.elementos.insert(posicion, elemento)

    def agregarElemento(self, elemento):
        self.elementos.append(elemento)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.elementos):
            raise IndexError("La posición dada no es válida para mostrar el elemento")
        return self.elementos[posicion]

def main():
    coleccion=MiColeccion()
    try:
        coleccion.insertarElemento("A", 0)
        coleccion.insertarElemento("B", 1)
        coleccion.insertarElemento("C", 3)  # Lanzará una excepción ValueError
    except ValueError as e:
        print(str(e))

    coleccion.agregarElemento("D")


    try:
        print(coleccion.mostrarElemento(2))
        print(coleccion.mostrarElemento(3))  # Lanzará una excepción IndexError
    except IndexError as e:
        print(str(e))

if __name__ == "__main__":
    main()