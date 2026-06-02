from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.socio import Socio


def test_buscar_libro_inexistente():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(Libro("1", "A", "X"))
    assert biblioteca.buscar_libro("999") is None


def test_buscar_socio_inexistente():
    biblioteca = Biblioteca()
    biblioteca.registrar_socio(Socio("1", "Ana"))
    assert biblioteca.buscar_socio("999") is None


def test_devolver_libro_sin_prestamo():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(Libro("1", "A", "X"))
    assert biblioteca.devolver_libro("1") is False


def test_listar_libros_vacio(capsys):
    biblioteca = Biblioteca()
    biblioteca.listar_libros()
    salida = capsys.readouterr().out
    assert "No hay libros registrados" in salida


def test_listar_socios_vacio(capsys):
    biblioteca = Biblioteca()
    biblioteca.listar_socios()
    salida = capsys.readouterr().out
    assert "No hay socios registrados" in salida