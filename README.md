# Biblioteca OO — Trabajo Práctico

Pequeño software orientado a objetos desarrollado como ejercicio de práctica. Contiene clases `Libro`, `Socio` y `Biblioteca` con operaciones básicas de préstamo.

Objetivos del repositorio:
- Proveer un ejemplo simple para pruebas unitarias, de integración y de rendimiento.

Cómo ejecutar (local):

1. Instalar dependencias (opcional):

```bash
python -m pip install -r requirements.txt
```

2. Ejecutar el programa principal:

```bash
python main.py
```

Estructura propuesta para pruebas:
- `tests/test_libro.py` — pruebas unitarias para `Libro`
- `tests/test_socio.py` — pruebas unitarias para `Socio`
- `tests/test_biblioteca.py` — pruebas de integración ligeras

Más artefactos (UML, resultados de tests) se añadirán en pasos posteriores.
# FINALTESTEO - Sistema de Gestión de Biblioteca

**Trabajo Práctico Final - Testing de Software**  
**Universidad de Belgrano** - Técnico en Programación de Computadoras

## 1.1 Descriptivo del Software

**Objetivo del Software:**  
Desarrollar un sistema simple orientado a objetos para la gestión de una biblioteca, permitiendo el registro de libros y socios, realización de préstamos y devoluciones con las validaciones correspondientes.

**Requerimientos Funcionales Implementados:**
- Alta, búsqueda y listado de Libros
- Alta y listado de Socios
- Realizar Préstamos (validando disponibilidad del libro y máximo 3 libros por socio)
- Devolución de Libros
- Listados completos

**Requerimientos No Funcionales:**
- Desarrollado en **Python 3** con Programación Orientada a Objetos
- Uso de Encapsulación
- Interfaz por consola intuitiva y amigable
- Código modular, legible y comentado

## 1.3 Artefactos UML

![Diagrama de Clases](UML.png)

## 1.4 Link al Repositorio

**Repositorio GitHub:**  
[https://github.com/Guidoolivero/FinalTesteo](https://github.com/Guidoolivero/FinalTesteo)

### Cómo ejecutar el programa

1. Descargás o copiás el repositorio.
2. Abrís una terminal en la raíz del proyecto: `/Users/guidoolivero/FinalTesteo`.
3. Ejecutás la aplicación con:

```bash
python3 main.py
```

### Cómo ejecutar los tests

Los tests se ejecutan desde la raíz del proyecto con `pytest`:

```bash
python3 -m pytest -q
```

No ejecutes los archivos dentro de `tests/` como scripts sueltos, porque eso puede dejar el paquete `biblioteca` fuera del `sys.path`.
