class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    # Getters
    def get_isbn(self) -> str:
        return self.__isbn

    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def esta_disponible(self) -> bool:
        return self.__disponible

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"ISBN: {self.__isbn} | {self.__titulo} - {self.__autor} [{estado}]"