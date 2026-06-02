# Pruebas End-to-End (E2E) - Biblioteca

**TP Final - Punto 4.1 (documentacion E2E)**  
**Universidad de Belgrano** - Tecnico en Programacion de Computadoras

## 1. Objetivo

Verificar el sistema completo desde la perspectiva del usuario: entradas del menu de consola, procesamiento por `main.py` y respuestas en pantalla, sin acceder al codigo interno durante la ejecucion del test.

## 2. Alcance

| Incluido | Excluido |
|----------|----------|
| Menu principal y opciones 0-6 | Pruebas unitarias de clases aisladas |
| Alta de libro y socio por consola | Pruebas de integracion directa sobre `Biblioteca` |
| Prestamo, devolucion y listados | Interfaz grafica o web |
| Validacion de mensajes al usuario | Rendimiento masivo (benchmark) |

## 3. Herramientas

- **Python 3**
- **pytest** con marker `e2e`
- **subprocess**: lanza `python main.py` y simula `stdin` como haria un usuario

Los tests estan en [`tests/test_e2e.py`](../tests/test_e2e.py).

## 4. Datos iniciales del programa

Al iniciar, `main.py` precarga:

- Libros: ISBN `001`, `002`, `003`
- Socios: DNI `12345678` (Juan Perez), DNI `87654321` (Ana Lopez)

Los escenarios E2E usan esos datos salvo cuando agregan libro o socio nuevos.

## 5. Matriz de casos de prueba

| ID | Test | Entrada (secuencia) | Resultado esperado |
|----|------|---------------------|--------------------|
| E2E-01 | `test_e2e_prestamo_exitoso` | `3` -> `001` -> `12345678` -> `0` | Mensaje de prestamo exitoso |
| E2E-02 | `test_e2e_prestamo_libro_no_disponible` | Prestamo de `001`, segundo prestamo del mismo ISBN | Libro no disponible en el segundo intento |
| E2E-03 | `test_e2e_devolucion_exitosa` | Prestamo + `4` devolver `001` + `0` | Libro devuelto corectamente |
| E2E-04 | `test_e2e_agregar_libro_y_listar` | Alta libro `999` + listar + `0` | Libo agregado y visible en listado |
| E2E-05 | `test_e2e_registrar_socio` | Alta socio + `0` | Socio registrado |
| E2E-06 | `test_e2e_opcion_invalida` | `99` + `0` | Opcion invalida |
| E2E-07 | `test_e2e_salir` | `0` | Mensaje de despedida y salida limpia |

## 6. Como ejecutar

Desde la raiz del proyecto:

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -v -m e2e
```

Para ejecutar toda la suite (unitarias, integracion y E2E):

```bash
python3 -m pytest -v
```

## 7. Evidencia de ejecucion

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

Suite completa (29 tests):

```text
============================== 29 passed in ~5s ==============================
```

## 8. Relacion con otros tipos de prueba

| Tipo | Archivo | Que valida |
|------|---------|------------|
| Componente | `tests/test_libro.py`, `tests/test_socio.py`, `tests/test_biblioteca_componente.py` | Metodos y reglas de cada clase |
| Integracion | `tests/test_biblioteca.py` | Interaccion entre `Biblioteca`, `Libro` y `Socio` |
| Caja negra | `tests/test_caja_negra.py` | Entrada/salida por API publica |
| Rendimiento | `tests/test_rendimiento.py` | Tiempos con `pytest-benchmark` |
| E2E | `tests/test_e2e.py` | Flujo completo usuario -> consola -> sistema |

Matriz general: [MATRIZ_PRUEBAS.md](MATRIZ_PRUEBAS.md)

## 9. Limitaciones conocidas

- Cada test inicia una nueva instancia del programa (no comparte estado entre tests).
- Timeout de 5 segundos por proceso para evitar bloqueos si falta la opcion `0` (Salir).
- Los mensajes de consola se validan por texto exacto (incluye typos como "Libo agregado").