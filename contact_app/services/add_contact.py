from data.contact import obtener_contactos

def agregar_contacto():
    print("\n--- ADD CONTACT ---")
    # Obtener lista de contactos existentes
    contactos = obtener_contactos()
    #Validar nombre
    while True:
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        if nombre.strip() == "":
            print("El nombre no puede estar vacío. Por favor, intente de nuevo.")
            continue
        if any(char.isdigit() for char in nombre):
            print("El nombre no puede contener números. Por favor, intente de nuevo.")
            continue
        if any(contacto['nombre'].lower() == nombre.lower() for contacto in contactos):
            print("El contacto ya existe. Por favor, intente de nuevo.")
            continue
        break
    # Validar teléfono y email
    while True:
        telefono = input("Ingrese el teléfono del nuevo contacto: ")
        if telefono.strip() == "":
            print("El teléfono no puede estar vacío. Por favor, intente de nuevo.")
            continue
        break
    while True:
        email = input("Ingrese el email del nuevo contacto: ")
        if email.strip() == "":
            print("El email no puede estar vacío. Por favor, intente de nuevo.")
            continue
        if "@" not in email or "." not in email:
            print("El email no es válido. Por favor, intente de nuevo.")
            continue
        break
    # Guardar contactos actualizados
    
    nuevo_contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    # Agregar el nuevo contacto a la lista
    contactos.append(nuevo_contacto)
    print(f"Contacto agregado: Nombre: {nombre}, Teléfono: {telefono}, Email: {email}")
    return nuevo_contacto