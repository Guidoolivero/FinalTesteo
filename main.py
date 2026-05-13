from biblioteca import Biblioteca
from libro import Libro
from socio import Socio

def main():
    biblioteca = Biblioteca()

    # Datos de prueba
    biblioteca.agregar_libro(Libro("001", "El Quijote", "Miguel de Cervantes"))
    biblioteca.agregar_libro(Libro("002", "1984", "George Orwell"))
    biblioteca.agregar_libro(Libro("003", "Cien años de soledad", "Gabriel García Márquez"))
    biblioteca.registrar_socio(Socio("12345678", "Juan Pérez"))
    biblioteca.registrar_socio(Socio("87654321", "Ana López"))

    while True:
        print("\n" + "="*40)
        print("       BIBLIOTECA OO - MENÚ PRINCIPAL")
        print("="*40)
        print("1. Agregar Libro")
        print("2. Registrar Socio")
        print("3. Realizar Préstamo")
        print("4. Devolver Libro")
        print("5. Listar Todos los Libros")
        print("6. Listar Socios")
        print("0. Salir")
        print("="*40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            biblioteca.agregar_libro(Libro(isbn, titulo, autor))
            print("✅ Libro agregado.")

        elif opcion == "2":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            biblioteca.registrar_socio(Socio(dni, nombre))
            print("✅ Socio registrado.")

        elif opcion == "3":
            isbn = input("ISBN del libro: ")
            dni = input("DNI del socio: ")
            biblioteca.realizar_prestamo(isbn, dni)

        elif opcion == "4":
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)

        elif opcion == "5":
            biblioteca.listar_libros()

        elif opcion == "6":
            biblioteca.listar_socios()

        elif opcion == "0":
            print("👋 ¡Gracias por usar BibliotecaOO!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()