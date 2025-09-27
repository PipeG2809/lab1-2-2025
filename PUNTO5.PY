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
                guardar_usuarios(usuarios)
                return f"Bienvenido {u['nombre']}."
            return "Contraseña incorrecta."
    return "Usuario no encontrado."

def usuarios_activos():
    usuarios = cargar_usuarios()
    activos = [u for u in usuarios if u.get("activo")]
    if not activos:
        return "No hay usuarios activos."
    return "Usuarios activos:\n" + "\n".join(f"- {u['nombre']} ({u['cedula']})" for u in activos)

if __name__ == "__main__":
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver usuarios activos")
        print("4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            print(registrar_usuario())
        elif opcion == "2":
            print(iniciar_sesion())
        elif opcion == "3":
            print(usuarios_activos())
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
