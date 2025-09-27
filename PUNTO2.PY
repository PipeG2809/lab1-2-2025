from json import dumps

ARCHIVO_USUARIOS = "usuarios.txt"

def registrar_usuario():
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

def guardar_usuario(usuario, archivo=ARCHIVO_USUARIOS):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(dumps(usuario, indent=4, ensure_ascii=False))
        print(f"Usuario guardado correctamente en {archivo}")
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")


if __name__ == "__main__":
    usuario = registrar_usuario()
    print("\nUsuario registrado en diccionario:")
    print(usuario)

    guardar_usuario(usuario)
