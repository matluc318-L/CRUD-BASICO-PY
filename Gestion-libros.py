libros = []

def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    fecha = input("Fecha de publicación: ")
    libros.append({
        "Título": titulo,
        "Autor": autor,
        "Género": genero,
        "Fecha": fecha
    })
    print("✅ Libro agregado correctamente.")

def listar_libros():
    if not libros:
        print("⚠ No hay libros registrados.")
    else:
        for i, libro in enumerate(libros, start=1):
            print(f"{i}. {libro['Título']} - {libro['Autor']} ({libro['Género']}, {libro['Fecha']})")

def actualizar_libro():
    listar_libros()
    if libros:
        try:
            idx = int(input("Número del libro a actualizar: ")) - 1
            if 0 <= idx < len(libros):
                libros[idx]["Título"] = input("Nuevo título: ")
                libros[idx]["Autor"] = input("Nuevo autor: ")
                libros[idx]["Género"] = input("Nuevo género: ")
                libros[idx]["Fecha"] = input("Nueva fecha: ")
                print("✅ Libro actualizado.")
            else:
                print("⚠ Índice inválido.")
        except ValueError:
            print("⚠ Debes ingresar un número.")

def eliminar_libro():
    listar_libros()
    if libros:
        try:
            idx = int(input("Número del libro a eliminar: ")) - 1
            if 0 <= idx < len(libros):
                libros.pop(idx)
                print("🗑 Libro eliminado.")
            else:
                print("⚠ Índice inválido.")
        except ValueError:
            print("⚠ Debes ingresar un número.")

while True:
    print("\n📚 Menú de gestión de libros:")
    print("1. Agregar libro")
    print("2. Ver libros")
    print("3. Actualizar libro")
    print("4. Eliminar libro")
    print("5. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        listar_libros()
    elif opcion == "3":
        actualizar_libro()
    elif opcion == "4":
        eliminar_libro()
    elif opcion == "5":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("⚠ Opción inválida.")
