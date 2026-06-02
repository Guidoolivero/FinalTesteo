# Matriz de pruebas — Biblioteca OO

| Tipo (TP) | Archivo | Tests | Comando |
|-----------|---------|-------|---------|
| Componente — Libro | `tests/test_libro.py` | 2 | `pytest tests/test_libro.py -v` |
| Componente — Socio | `tests/test_socio.py` | 1 | `pytest tests/test_socio.py -v` |
| Componente — Biblioteca | `tests/test_biblioteca_componente.py` | 5 | `pytest tests/test_biblioteca_componente.py -v` |
| Integración | `tests/test_biblioteca.py` | 2 | `pytest tests/test_biblioteca.py -v` |
| Caja negra | `tests/test_caja_negra.py` | 8 | `pytest -m caja_negra -v` |
| Rendimiento | `tests/test_rendimiento.py` | 4 | `pytest tests/test_rendimiento.py -v --benchmark-only` |
| Interfaz (consola) | `tests/test_e2e.py` | ver tabla E2E | `pytest -m e2e -v` |
| Camino (flujos) | `tests/test_e2e.py` | ver tabla E2E | `pytest -m e2e -v` |
| End-to-End | `tests/test_e2e.py` | 7 | `pytest -m e2e -v` |

## Caja negra — entrada / salida observable

| Test | Entrada | Salida esperada |
|------|---------|-----------------|
| `test_cb_prestamo_exitoso_cambia_disponibilidad` | ISBN y DNI válidos | `True`; libro no disponible |
| `test_cb_prestamo_libro_inexistente` | ISBN inexistente | `False` |
| `test_cb_prestamo_socio_inexistente` | DNI inexistente | `False` |
| `test_cb_prestamo_libro_ocupado` | Segundo préstamo del mismo ISBN | `False` |
| `test_cb_limite_tres_prestamos_por_socio` | Cuarto préstamo al mismo socio | `False` |
| `test_cb_devolucion_restaura_disponibilidad` | Devolver ISBN prestado | `True`; libro disponible |
| `test_cb_devolucion_sin_prestamo_previo` | Devolver sin préstamo | `False` |
| `test_cb_busquedas_sin_datos` | Búsqueda en biblioteca vacía | `None` |

## Interfaz y camino (E2E)

| Test E2E | Interfaz | Camino |
|----------|----------|--------|
| `test_e2e_prestamo_exitoso` | Menú opción 3 | Camino feliz préstamo |
| `test_e2e_prestamo_libro_no_disponible` | Menú opción 3 | Camino alternativo / error |
| `test_e2e_devolucion_exitosa` | Menú opción 4 | Camino devolución |
| `test_e2e_agregar_libro_y_listar` | Opciones 1 y 5 | Alta + consulta |
| `test_e2e_registrar_socio` | Opción 2 | Alta socio |
| `test_e2e_opcion_invalida` | Entrada inválida | Manejo de error UI |
| `test_e2e_salir` | Opción 0 | Fin del programa |

## Rendimiento (referencia local)

Ejecutado con `pytest tests/test_rendimiento.py -v --benchmark-only` (junio 2026):

| Operación | Tiempo medio aprox. |
|-----------|---------------------|
| Buscar 1 libro entre 1000 | ~10 µs |
| Registrar 200 socios | ~48 µs |
| Agregar 1000 libros | ~332 µs |
| 100 préstamos seguidos | ~495 µs |

Los valores varían según el equipo; lo relevante es que las operaciones permanecen en escala de microsegundos/milisegundos para este volumen de datos.