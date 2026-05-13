from libro import Libro

class Socio:
    def __init__(self, dni: str, nombre: str):
        self.__dni = dni
        self.__nombre = nombre
        self.__libros_prestados: list[Libro] = []

    def get_dni(self) -> str:
        return self.__dni

    def get_nombre(self) -> str:
        return self.__nombre

    def get_libros_prestados(self) -> list:
        return self.__libros_prestados

    def puede_pedir_prestado(self) -> bool:
        return len(self.__libros_prestados) < 3

    def agregar_prestamo(self, libro: Libro):
        self.__libros_prestados.append(libro)

    def devolver_libro(self, libro: Libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    def __str__(self):
        return f"Socio: {self.__nombre} (DNI: {self.__dni}) - Libros prestados: {len(self.__libros_prestados)}"