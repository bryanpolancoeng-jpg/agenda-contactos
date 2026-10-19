"""Agenda de contactos en consola (versión original, sin bibliotecas)."""

CONTACTOS = [
    {"nombre": "John Smith", "telefono": "7777-1111", "correo": "john@example.com"},
    {"nombre": "María López", "telefono": "7777-2222", "correo": "maria@example.com"},
    {"nombre": "Carlos Hernández", "telefono": "7777-3333", "correo": "carlos@example.com"},
    {"nombre": "Ana Martínez", "telefono": "7777-4444", "correo": "ana@example.com"},
    {"nombre": "Jonathan Pérez", "telefono": "7777-5555", "correo": "jonathan@example.com"},
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


def buscar(texto):
    """Búsqueda manual: solo encuentra si el texto está escrito exactamente igual."""
    texto = texto.lower()
    resultados = []
    for c in CONTACTOS:
        if texto in c["nombre"].lower():
            resultados.append(c)
    return resultados


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
            resultados = buscar(texto)
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