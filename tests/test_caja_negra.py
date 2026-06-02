import pytest

from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.socio import Socio


@pytest.fixture
def biblioteca_vacia():
    return Biblioteca()


@pytest.fixture
def biblioteca_operativa():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(Libro("10", "Novela", "Autor A"))
    biblioteca.agregar_libro(Libro("20", "Ensayo", "Autor B"))
    biblioteca.agregar_libro(Libro("30", "Poesia", "Autor C"))
    biblioteca.agregar_libro(Libro("40", "Cuento", "Autor D"))
    biblioteca.registrar_socio(Socio("1001", "Carlos"))
    biblioteca.registrar_socio(Socio("1002", "Laura"))
    return biblioteca


@pytest.mark.caja_negra
def test_cb_prestamo_exitoso_cambia_disponibilidad(biblioteca_operativa):
    resultado = biblioteca_operativa.realizar_prestamo("10", "1001")

    libro = biblioteca_operativa.buscar_libro("10")
    assert resultado is True
    assert libro is not None
    assert libro.esta_disponible() is False


@pytest.mark.caja_negra
def test_cb_prestamo_libro_inexistente(biblioteca_operativa):
    assert biblioteca_operativa.realizar_prestamo("999", "1001") is False


@pytest.mark.caja_negra
def test_cb_prestamo_socio_inexistente(biblioteca_operativa):
    assert biblioteca_operativa.realizar_prestamo("10", "9999") is False


@pytest.mark.caja_negra
def test_cb_prestamo_libro_ocupado(biblioteca_operativa):
    assert biblioteca_operativa.realizar_prestamo("10", "1001") is True
    assert biblioteca_operativa.realizar_prestamo("10", "1002") is False


@pytest.mark.caja_negra
def test_cb_limite_tres_prestamos_por_socio(biblioteca_operativa):
    assert biblioteca_operativa.realizar_prestamo("10", "1001") is True
    assert biblioteca_operativa.realizar_prestamo("20", "1001") is True
    assert biblioteca_operativa.realizar_prestamo("30", "1001") is True
    assert biblioteca_operativa.realizar_prestamo("40", "1001") is False


@pytest.mark.caja_negra
def test_cb_devolucion_restaura_disponibilidad(biblioteca_operativa):
    biblioteca_operativa.realizar_prestamo("10", "1001")
    assert biblioteca_operativa.devolver_libro("10") is True

    libro = biblioteca_operativa.buscar_libro("10")
    assert libro is not None
    assert libro.esta_disponible() is True


@pytest.mark.caja_negra
def test_cb_devolucion_sin_prestamo_previo(biblioteca_operativa):
    assert biblioteca_operativa.devolver_libro("10") is False


@pytest.mark.caja_negra
def test_cb_busquedas_sin_datos(biblioteca_vacia):
    assert biblioteca_vacia.buscar_libro("1") is None
    assert biblioteca_vacia.buscar_socio("1") is None