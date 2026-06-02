import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_cli(stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "main.py"],
        input=stdin,
        text=True,
        capture_output=True,
        cwd=PROJECT_ROOT,
        timeout=5,
        check=False,
    )


@pytest.mark.e2e
def test_e2e_prestamo_exitoso():
    result = run_cli("3\n001\n12345678\n0\n")
    assert result.returncode == 0
    assert "Préstamo realizado con éxito" in result.stdout


@pytest.mark.e2e
def test_e2e_prestamo_libro_no_disponible():
    result = run_cli("3\n001\n12345678\n3\n001\n87654321\n0\n")
    assert result.returncode == 0
    assert "Préstamo realizado con éxito" in result.stdout
    assert "no está disponible" in result.stdout


@pytest.mark.e2e
def test_e2e_devolucion_exitosa():
    result = run_cli("3\n001\n12345678\n4\n001\n0\n")
    assert result.returncode == 0
    assert "Libro devuelto correctamente" in result.stdout


@pytest.mark.e2e
def test_e2e_agregar_libro_y_listar():
    result = run_cli("1\n999\nObra Nueva\nAutor Test\n5\n0\n")
    assert result.returncode == 0
    assert "Libro agregado" in result.stdout
    assert "999" in result.stdout
    assert "Obra Nueva" in result.stdout


@pytest.mark.e2e
def test_e2e_registrar_socio():
    result = run_cli("2\n11223344\nMaría Test\n0\n")
    assert result.returncode == 0
    assert "Socio registrado" in result.stdout


@pytest.mark.e2e
def test_e2e_opcion_invalida():
    result = run_cli("99\n0\n")
    assert result.returncode == 0
    assert "Opción inválida" in result.stdout


@pytest.mark.e2e
def test_e2e_salir():
    result = run_cli("0\n")
    assert result.returncode == 0
    assert "Gracias por usar BibliotecaOO" in result.stdout