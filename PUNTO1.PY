def registrar_usuario():
    """Solicita al usuario su información de registro y la almacena en un diccionario"""
    cedula = input("Ingrese su cédula: ")
    nombre = input("Ingrese su nombre: ")
    apellidos = input("Ingrese sus apellidos: ")
    contraseña = input("Ingrese su contraseña: ")
    usuario = {
        "cedula": cedula,
        "nombre": nombre,
        "apellidos": apellidos,
        "contraseña": contraseña,
    }

    return usuario

if __name__ == "__main__":
    usuario = registrar_usuario()
    print("\nUsuario registrado en diccionario:")
    print(usuario)
