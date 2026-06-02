# Pruebas End-to-End (E2E) — Biblioteca OO

**TP Final — Punto 4.1 (documentación E2E)**  
**Universidad de Belgrano** — Técnico en Programación de Computadoras

## 1. Objetivo

Verificar el sistema completo desde la perspectiva del usuario: entradas del menú de consola, procesamiento por `main.py` y respuestas en pantalla, sin acceder al código interno durante la ejecución del test.

## 2. Alcance

| Incluido | Excluido |
|----------|----------|
| Menú principal y opciones 0–6 | Pruebas unitarias de clases aisladas |
| Alta de libro y socio por consola | Pruebas de integración directa sobre `Biblioteca` |
| Préstamo, devolución y listados | Interfaz gráfica o web |
| Validación de mensajes al usuario | Rendimiento masivo (benchmark) |

## 3. Herramientas

- **Python 3**
- **pytest** con marker `e2e`
- **subprocess**: lanza `python main.py` y simula `stdin` como haría un usuario

Los tests están en [`tests/test_e2e.py`](../tests/test_e2e.py).

## 4. Datos iniciales del programa

Al iniciar, `main.py` precarga:

- Libros: ISBN `001`, `002`, `003`
- Socios: DNI `12345678` (Juan Pérez), DNI `87654321` (Ana López)

Los escenarios E2E usan esos datos salvo cuando agregan libro o socio nuevos.

## 5. Matriz de casos de prueba

| ID | Test | Entrada (secuencia) | Resultado esperado |
|----|------|---------------------|--------------------|
| E2E-01 | `test_e2e_prestamo_exitoso` | `3` → `001` → `12345678` → `0` | Mensaje de préstamo exitoso |
| E2E-02 | `test_e2e_prestamo_libro_no_disponible` | Préstamo de `001`, segundo préstamo del mismo ISBN | Libro no disponible en el segundo intento |
| E2E-03 | `test_e2e_devolucion_exitosa` | Préstamo + `4` devolver `001` + `0` | Libro devuelto correctamente |
| E2E-04 | `test_e2e_agregar_libro_y_listar` | Alta libro `999` + listar + `0` | Libro agregado y visible en listado |
| E2E-05 | `test_e2e_registrar_socio` | Alta socio + `0` | Socio registrado |
| E2E-06 | `test_e2e_opcion_invalida` | `99` + `0` | Opción inválida |
| E2E-07 | `test_e2e_salir` | `0` | Mensaje de despedida y salida limpia |

## 6. Cómo ejecutar

Desde la raíz del proyecto:

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -v -m e2e
```

Para ejecutar toda la suite (unitarias, integración y E2E):

```bash
python3 -m pytest -v
```

## 7. Evidencia de ejecución

**Fecha:** 2 de junio de 2026

```text
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/guidoolivero/FinalTesteo
configfile: pytest.ini
collecting ... collected 12 items / 5 deselected / 7 selected

tests/test_e2e.py::test_e2e_prestamo_exitoso PASSED                      [ 14%]
tests/test_e2e.py::test_e2e_prestamo_libro_no_disponible PASSED          [ 28%]
tests/test_e2e.py::test_e2e_devolucion_exitosa PASSED                    [ 42%]
tests/test_e2e.py::test_e2e_agregar_libro_y_listar PASSED                [ 57%]
tests/test_e2e.py::test_e2e_registrar_socio PASSED                       [ 71%]
tests/test_e2e.py::test_e2e_opcion_invalida PASSED                       [ 85%]
tests/test_e2e.py::test_e2e_salir PASSED                                 [100%]

======================= 7 passed, 5 deselected in 0.12s ========================
```

Suite completa:

```text
tests/test_biblioteca.py::test_prestamo_exitoso PASSED
tests/test_biblioteca.py::test_prestamo_fallos PASSED
tests/test_e2e.py::test_e2e_prestamo_exitoso PASSED
tests/test_e2e.py::test_e2e_prestamo_libro_no_disponible PASSED
tests/test_e2e.py::test_e2e_devolucion_exitosa PASSED
tests/test_e2e.py::test_e2e_agregar_libro_y_listar PASSED
tests/test_e2e.py::test_e2e_registrar_socio PASSED
tests/test_e2e.py::test_e2e_opcion_invalida PASSED
tests/test_e2e.py::test_e2e_salir PASSED
tests/test_libro.py::test_libro_getters_y_estado PASSED
tests/test_libro.py::test_prestar_devolver PASSED
tests/test_socio.py::test_socio_prestamo_y_limite PASSED

============================== 12 passed in 0.12s ==============================
```

## 8. Relación con otros tipos de prueba

| Tipo | Archivo | Qué valida |
|------|---------|------------|
| Componente | `tests/test_libro.py`, `tests/test_socio.py`, `tests/test_biblioteca_componente.py` | Métodos y reglas de cada clase |
| Integración | `tests/test_biblioteca.py` | Interacción entre `Biblioteca`, `Libro` y `Socio` |
| Caja negra | `tests/test_caja_negra.py` | Entrada/salida por API pública |
| Rendimiento | `tests/test_rendimiento.py` | Tiempos con `pytest-benchmark` |
| E2E | `tests/test_e2e.py` | Flujo completo usuario → consola → sistema |

Matriz general: [MATRIZ_PRUEBAS.md](MATRIZ_PRUEBAS.md)

## 9. Limitaciones conocidas

- Cada test inicia una nueva instancia del programa (no comparte estado entre tests).
- Timeout de 5 segundos por proceso para evitar bloqueos si falta la opción `0` (Salir).
- Los emojis en la salida de consola se validan por texto; en terminales muy antiguas la visualización puede variar sin afectar la lógica del sistema.