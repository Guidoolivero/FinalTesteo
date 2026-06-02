import pytest

from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.socio import Socio

CANTIDAD_LIBROS = 1000
CANTIDAD_SOCIOS = 200
CANTIDAD_PRESTAMOS = 100


def _biblioteca_con_libros(cantidad: int) -> Biblioteca:
    biblioteca = Biblioteca()
    for i in range(cantidad):
        biblioteca.agregar_libro(Libro(f"{i:04d}", f"Titulo {i}", f"Autor {i}"))
    return biblioteca


def _biblioteca_para_prestamos() -> Biblioteca:
    biblioteca = _biblioteca_con_libros(CANTIDAD_PRESTAMOS)
    for i in range(CANTIDAD_PRESTAMOS):
        biblioteca.registrar_socio(Socio(f"{i:08d}", f"Socio {i}"))
    return biblioteca


@pytest.mark.benchmark
def test_rendimiento_agregar_muchos_libros(benchmark):
    def cargar():
        biblioteca = Biblioteca()
        for i in range(CANTIDAD_LIBROS):
            biblioteca.agregar_libro(Libro(f"{i:04d}", f"Titulo {i}", f"Autor {i}"))

    benchmark(cargar)


@pytest.mark.benchmark
def test_rendimiento_buscar_libro(benchmark):
    biblioteca = _biblioteca_con_libros(CANTIDAD_LIBROS)
    benchmark(biblioteca.buscar_libro, "0500")


@pytest.mark.benchmark
def test_rendimiento_registrar_socios(benchmark):
    def cargar():
        biblioteca = Biblioteca()
        for i in range(CANTIDAD_SOCIOS):
            biblioteca.registrar_socio(Socio(f"{i:08d}", f"Socio {i}"))

    benchmark(cargar)


@pytest.mark.benchmark
def test_rendimiento_prestamos_seguidos(benchmark):
    biblioteca = _biblioteca_para_prestamos()

    def prestar_todos():
        for i in range(CANTIDAD_PRESTAMOS):
            biblioteca.realizar_prestamo(f"{i:04d}", f"{i:08d}")

    benchmark(prestar_todos)