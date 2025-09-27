import json
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
        # Intentar leer el archivo
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
        except FileNotFoundError:
            usuarios = []
        except json.JSONDecodeError:
            usuarios = []

        # Si usuarios no es lista (ej: un dict), convertirlo en lista
        if isinstance(usuarios, dict):
            usuarios = [usuarios]

        # Verificar duplicados
        for u in usuarios:
            if u["cedula"] == usuario["cedula"]:
                return f"Error: el usuario con cédula {usuario['cedula']} ya existe."

        # Agregar nuevo usuario
        usuarios.append(usuario)

        # Guardar nuevamente la lista
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(dumps(usuarios, indent=4, ensure_ascii=False))

        return f"Usuario {usuario['nombre']} registrado correctamente."

    except Exception as e:
        return f"Error al guardar el usuario: {e}"


if __name__ == "__main__":
    usuario = registrar_usuario()
    print("\nUsuario registrado en diccionario:")
    print(usuario)

    resultado = guardar_usuario(usuario)
    print(resultado)

