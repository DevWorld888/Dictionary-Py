from services.show_contacts import mostrar_contactos

def main():
    while True:
        from utils.menu import Show_menu
        choice = Show_menu()
        
        if choice == '1':
            mostrar_contactos()
        elif choice == '2':
            from services.search_contact import buscar_contacto_por_nombre
            buscar_contacto_por_nombre()
        elif choice == '3':
            from services.add_contact import agregar_contacto
            agregar_contacto()
        elif choice == '4':
            from services.delete_contact import delete_contact_by_name
            delete_contact_by_name()
        elif choice == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()