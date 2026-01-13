from data.contact import obtener_contactos

def delete_contact_by_name():
    contactos = obtener_contactos()
    name = input("Ingrese el nombre del contacto a eliminar: ")
    for i, contacto in enumerate(contactos):
        if contacto['nombre'].lower() == name.lower():
            deleted_contact = contactos.pop(i)
            print(f"Contacto eliminado: Nombre: {deleted_contact['nombre']}, Teléfono: {deleted_contact['telefono']}, Email: {deleted_contact['email']}")
            return deleted_contact
    print("Contacto no encontrado.")