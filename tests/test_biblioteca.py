from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.socio import Socio


import pytest


@pytest.fixture
def biblioteca_basica():
    b = Biblioteca()
    b.agregar_libro(Libro("1", "A", "X"))
    b.registrar_socio(Socio("1", "Juan"))
    return b


def test_prestamo_exitoso(biblioteca_basica):
    assert biblioteca_basica.realizar_prestamo("1", "1") is True


def test_prestamo_fallos(biblioteca_basica):
    # libro inexistente
    assert biblioteca_basica.realizar_prestamo("999", "1") is False
    # socio inexistente
    assert biblioteca_basica.realizar_prestamo("1", "999") is False
