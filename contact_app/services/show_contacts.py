from data.contact import obtener_contactos

def mostrar_contactos():
    contactos = obtener_contactos()
    print("\n--- SHOW CONTACTS ---")
    print("1. Sort by name")
    print("2. Sort by phone")
    print("3. Sort by email")
    print("4. Show without sorting")
    option = input("Choose an option: ")
    if option == '1':
        contactos.sort(key=lambda x: x['nombre'])
    elif option == '2':
        contactos.sort(key=lambda x: x['telefono'])
    elif option == '3':
        contactos.sort(key=lambda x: x['email'])
    elif option != '4':
        print("Invalid option. Showing without sorting.")
    print("\n--- CONTACT LIST ---")
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")