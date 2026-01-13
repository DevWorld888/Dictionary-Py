from data.contact import obtener_contactos

def agregar_contacto():
    contactos = obtener_contactos()
    nombre = input("Ingrese el nombre del nuevo contacto: ")
    telefono = input("Ingrese el teléfono del nuevo contacto: ")
    email = input("Ingrese el email del nuevo contacto: ")
    
    nuevo_contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    
    contactos.append(nuevo_contacto)
    print(f"Contacto agregado: Nombre: {nombre}, Teléfono: {telefono}, Email: {email}")
    return nuevo_contacto