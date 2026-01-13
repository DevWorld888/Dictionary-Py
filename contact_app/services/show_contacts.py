from data.contact import obtener_contactos

def mostrar_contactos():
    contactos = obtener_contactos()
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")