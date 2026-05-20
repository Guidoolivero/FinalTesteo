from libro import Libro
from socio import Socio

class Biblioteca:
    def __init__(self):
        self.__libros: list[Libro] = []
        self.__socios: list[Socio] = []

    def agregar_libro(self, libro: Libro):
        self.__libros.append(libro)

    def registrar_socio(self, socio: Socio):
        self.__socios.append(socio)

    def buscar_libro(self, isbn: str) -> Libro | None:
        for libro in self.__libros:
            if libro.get_isbn() == isbn:
                return libro
        return None

    def buscar_socio(self, dni: str) -> Socio | None:
        for socio in self.__socios:
            if socio.get_dni() == dni:
                return socio
        return None

    def realizar_prestamo(self, isbn: str, dni: str) -> bool:
        libro = self.buscar_libro(isbn)
        socio = self.buscar_socio(dni)

        if not libro or not socio:
            print("❌ Libro o socio no encontrado.")
            return False
        if not libro.esta_disponible():
            print("❌ El libro no está disponible.")
            return False
        if not socio.puede_pedir_prestado():
            print("❌ El socio ya tiene el máximo de libros permitidos (3).")
            return False

        libro.prestar()
        socio.agregar_prestamo(libro)
        print("✅ Préstamo realizado con éxito.")
        return True

    def devolver_libro(self, isbn: str) -> bool:
        libro = self.buscar_libro(isbn)
        if not libro or libro.esta_disponible():
            print("❌ Libro no encontrado o ya está disponible.")
            return False

        for socio in self.__socios:
            if libro in socio.get_libros_prestados():
                libro.devolver()
                socio.devolver_libro(libro)
                print("✅ Libro devuelto correctamente.")
                return True
        return False

    def listar_libros(self):
        if not self.__libros:
            print("No hay libros registrados.")
            return
        for libro in self.__libros:
            print(libro)

    def listar_socios(self):
        if not self.__socios:
            print("No hay socios registrados.")
            return
        for socio in self.__socios:
            print(socio)