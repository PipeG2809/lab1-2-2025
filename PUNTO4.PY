import json
from json import dumps

ARCHIVO = "usuarios.txt"

def cargar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]
    except:
        return []

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write(dumps(usuarios, indent=4, ensure_ascii=False))

def registrar_usuario():
    usuario = {
        "cedula": input("Cédula: "),
        "nombre": input("Nombre: "),
        "apellidos": input("Apellidos: "),
        "contraseña": input("Contraseña: "),
        "activo": False
    }
    usuarios = cargar_usuarios()
    if any(u["cedula"] == usuario["cedula"] for u in usuarios):
        return f"Error: cédula {usuario['cedula']} ya registrada."
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    return f"Usuario {usuario['nombre']} registrado."

def iniciar_sesion():
    cedula = input("Cédula: ")
    contraseña = input("Contraseña: ")
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u["cedula"] == cedula:
            if u["contraseña"] == contraseña:
                u["activo"] = True
                u["ip"] = "127.0.0.1"
                guardar_usuarios(usuarios)
                return f"Bienvenido {u['nombre']}."
            return "Contraseña incorrecta."
    return "Usuario no encontrado."

if __name__ == "__main__":
    print("1. Registrar\n2. Iniciar sesión")
    opcion = input("Opción: ")
    print(registrar_usuario() if opcion=="1" else iniciar_sesion())

