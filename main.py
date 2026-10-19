from busqueda import buscar_contactos

CONTACTOS = [
    {"nombre": "John Smith", "telefono": "7777-1111", "correo": "john@utla.com"},
    {"nombre": "María López", "telefono": "7777-2222", "correo": "maria@utla.com"},
    {"nombre": "Carlos Hernández", "telefono": "7777-3333", "correo": "carlos@utla.com"},
    {"nombre": "Ana Martínez", "telefono": "7777-4444", "correo": "ana@utla.com"},
    {"nombre": "Jonathan Pérez", "telefono": "7777-5555", "correo": "jonathan@jonathan.com"},
]


def mostrar(contacto):
    print(f"  {contacto['nombre']} | {contacto['telefono']} | {contacto['correo']}")


def listar():
    print("\n--- Todos los contactos ---")
    for c in CONTACTOS:
        mostrar(c)


def agregar():
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    CONTACTOS.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    print("Contacto agregado.")


def menu():
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Listar contactos")
        print("2. Agregar contacto")
        print("3. Buscar contacto")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            listar()
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            texto = input("Buscar: ").strip()

            resultados = buscar_contactos(texto, CONTACTOS)

            if resultados:
                print("\n--- Resultados ---")
                for c in resultados:
                    mostrar(c)
            else:
                print("No se encontraron contactos.")
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()