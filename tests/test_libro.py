from biblioteca.libro import Libro


def test_libro_getters_y_estado():
    l = Libro("001", "El Quijote", "Cervantes")
    assert l.get_isbn() == "001"
    assert "Quijote" in l.get_titulo()
    assert l.esta_disponible() is True


def test_prestar_devolver():
    l = Libro("002", "1984", "Orwell")
    l.prestar()
    assert not l.esta_disponible()
    l.devolver()
    assert l.esta_disponible()
