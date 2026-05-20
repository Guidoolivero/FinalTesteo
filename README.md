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

Cómo ejecutar (local):

1. Instalar dependencias (opcional):

```bash
python -m pip install -r requirements.txt
```

2. Ejecutar el programa principal:

```bash
python main.py
```

## 2. Diseño de un conjunto de Pruebas

Se diseñaron distintas pruebas para verificar que el sistema funcione correctamente.

### 2.1 Prueba de componentes
Se probaron de forma individual cada clase y sus métodos principales:
- Clase `Libro`
- Clase `Socio`
- Clase `Biblioteca`

### 2.2 Prueba de Integración
Se verificó que las clases interactúen correctamente entre sí (por ejemplo: registrar un socio y luego realizarle un préstamo).

### 2.3 Prueba de Caja Negra
Se probaron las funcionalidades del sistema según su comportamiento esperado, sin mirar el código interno.

### 2.4 Prueba de Rendimiento
Se comprobó que el sistema responda de forma rápida al agregar múltiples libros y socios.

### 2.5 Prueba de Interfaz
Se verificó que el menú de consola sea claro, fácil de usar y maneje correctamente las entradas del usuario.

### 2.6 Prueba de Camino
Se probaron los caminos principales del programa (préstamo exitoso, préstamo fallido, devolución de libro, etc.).

### Cómo ejecutar los tests

Los tests se ejecutan desde la raíz del proyecto con **pytest**:

```bash
python3 -m pytest -q
```

## 3. Planificar la ejecución de las Pruebas

### 3.1 Planificación de la ejecución

Se planificó ejecutar las pruebas de forma automática con **pytest**.

**Orden de ejecución:**
1. Pruebas unitarias de `Libro`
2. Pruebas unitarias de `Socio`
3. Pruebas de integración de `Biblioteca`

**Comando utilizado:**
```bash
python3 -m pytest -v
```
### 3.2 Ejecución de las Pruebas y Documentación

Fecha de ejecución: 20 de mayo de 2026

Salida obtenida:

| Test | Tipo de prueba | Resultado |
|---|---|---|
| tests/test_biblioteca.py::test_prestamo_exitoso | Integracion | PASSED |
| tests/test_biblioteca.py::test_prestamo_fallos | Integracion | PASSED |
| tests/test_libro.py::test_libro_getters_y_estado | Unitaria | PASSED |
| tests/test_libro.py::test_prestar_devolver | Unitaria | PASSED |
| tests/test_socio.py::test_socio_prestamo_y_limite | Unitaria | PASSED |

5 passed in 0.01s

