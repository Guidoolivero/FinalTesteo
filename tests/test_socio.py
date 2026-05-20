import pytest
from biblioteca.socio import Socio
from biblioteca.libro import Libro


@pytest.fixture
def libro():
    return Libro("100", "Título", "Autor")


def test_socio_prestamo_y_limite(libro):
    s = Socio("123", "Ana")
    assert s.get_dni() == "123"
    assert s.puede_pedir_prestado() is True
    s.agregar_prestamo(libro)
    assert len(s.get_libros_prestados()) == 1
    # Simular límite
    for i in range(2):
        s.agregar_prestamo(Libro(str(200+i), "T", "A"))
    assert s.puede_pedir_prestado() is False
    s.devolver_libro(libro)
    assert libro not in s.get_libros_prestados()
