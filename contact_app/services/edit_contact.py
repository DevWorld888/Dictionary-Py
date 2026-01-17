from data.contact import obtener_contactos

def editar_contacto():
    print("\n--- EDIT CONTACT ---")
    contactos = obtener_contactos()
    nombre_buscar = input("Ingrese el nombre del contacto que desea editar: ")

    for contacto in contactos:
        if contacto['nombre'].lower() == nombre_buscar.lower():
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            # Solicitar nuevos datos
            nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
            nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
            nuevo_email = input("Ingrese el nuevo email (deje en blanco para no cambiar): ")

            # Actualizar datos si se proporcionaron nuevos valores
            if nuevo_nombre.strip():
                contacto['nombre'] = nuevo_nombre
            if nuevo_telefono.strip():
                contacto['telefono'] = nuevo_telefono
            if nuevo_email.strip():
                contacto['email'] = nuevo_email

            print(f"Contacto actualizado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            return contacto
    print("Contacto no encontrado.")