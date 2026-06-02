from biblioteca import Biblioteca, Libro, Socio

def main():
    biblioteca = Biblioteca()

    # Datos iniciales de ejemplo
    biblioteca.agregar_libro(Libro("001", "Introduccion a Python", "M. Rodriguez"))
    biblioteca.agregar_libro(Libro("002", "Base de Datos I", "Prof. Garcia"))
    biblioteca.agregar_libro(Libro("003", "Testeo de Software", "Catedra UB"))
    biblioteca.registrar_socio(Socio("12345678", "Juan Perez"))
    biblioteca.registrar_socio(Socio("87654321", "Ana Lopez"))

    while True:
        print("\n" + "="*40)
        print("     GESTION DE BIBLIOTECA - MENU")
        print("="*40)
        print("1. Agregar Libro")
        print("2. Registrar Socio")
        print("3. Realizar Prestamo")
        print("4. Devolver Libro")
        print("5. Listar Todos los Libros")
        print("6. Listar Socios")
        print("0. Salir")
        print("="*40)

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            isbn = input("ISBN: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            biblioteca.agregar_libro(Libro(isbn, titulo, autor))
            print("Libo agregado.")

        elif opcion == "2":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            biblioteca.registrar_socio(Socio(dni, nombre))
            print("Socio registrado.")

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
            print("Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()