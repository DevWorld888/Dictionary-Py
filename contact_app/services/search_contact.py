from data.contact import obtener_contactos

def buscar_contacto_por_nombre(nombre):
    contactos = obtener_contactos()
    name = input("Ingrese el nombre del contacto a buscar: ")
    for contacto in contactos:
        if contacto['nombre'].lower() == name.lower():
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            return contacto
    print("Contacto no encontrado.")
    