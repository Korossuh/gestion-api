import requests
import json
import sys

#URL para la api
BASE_URL = "http://127.0.0.1:8000/api/"

#funcion para Verificar si la api esta en funcionamiento
#Para verificar si tengo andando el proyecto o no 
def verificar_api():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            return True
        else:
            print(f"Error al conectar con la API. Código de estado: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"No se pudo conectar a la API: {e}")
        return False

#funcion para Menú Principal
def menu_principal():
    print("==== Menú Principal ====")
    print("1. Ver datos")
    print("2. Subir datos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_ver_datos()
    elif opcion == "2":
        menu_subir_datos()
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción inválida.")
        menu_principal()

#funcion para Menú ver datos
def menu_ver_datos():
    print("\n==== Ver Datos ====")
    print("1. Personas")
    print("2. Proyectos")
    print("3. Tareas")
    print("4. Comentarios")
    print("5. Documentos")
    print("6. Volver al menú principal")
    opcion = input("Seleccione una opción: ")

    endpoints = {
        "1": "personas/",
        "2": "proyectos/",
        "3": "tareas/",
        "4": "comentarios/",
        "5": "documentos/"
    }

    if opcion in endpoints:
        obtener_datos(endpoints[opcion])
    elif opcion == "6":
        menu_principal()
    else:
        print("Opción inválida.")
        menu_ver_datos()

#funcion para Menú de subir datos
def menu_subir_datos():
    print("\n==== Subir Datos ====")
    print("1. Persona")
    print("2. Proyecto")
    print("3. Tarea")
    print("4. Comentario")
    print("5. Documento")
    print("6. Volver al menú principal")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        subir_persona()
    elif opcion == "2":
        subir_proyecto()
    elif opcion == "3":
        subir_tarea()
    elif opcion == "4":
        subir_comentario()
    elif opcion == "5":
        subir_documento()
    elif opcion == "6":
        menu_principal()
    else:
        print("Opción inválida.")
        menu_subir_datos()

#funcion para obtener los datos
def obtener_datos(endpoint):
    url = BASE_URL + endpoint
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            print(json.dumps(datos, indent=4))
        else:
            print("Error al obtener los datos:", response.status_code)
    except Exception as e:
        print("Error al conectarse a la API:", str(e))
    finally:
        menu_ver_datos()

#funcion para validar Campos
def validar_campos(datos, campos_obligatorios):
    for campo in campos_obligatorios:
        if not datos.get(campo):
            print(f"El campo {campo} es obligatorio.")
            return False
    return True

# Funciones para subir Personas
def subir_persona():
    print("\n--- SUBIR NUEVA PERSONA ---")
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono (opcional): ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD, opcional): ")

    payload = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono if telefono else None,
        "fecha_nacimiento": fecha_nacimiento if fecha_nacimiento else None
    }

    if validar_campos(payload, ["nombre", "email"]):
        enviar_datos("personas/", payload)

#funcion para subir Proyectos
def subir_proyecto():
    print("\n--- SUBIR NUEVO PROYECTO ---")
    nombre = input("Nombre del proyecto: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de fin (YYYY-MM-DD, opcional): ")
    persona_responsable = input("ID de la persona responsable: ")

    payload = {
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin if fecha_fin else None,
        "persona_responsable": persona_responsable
    }

    if validar_campos(payload, ["nombre", "descripcion", "fecha_inicio", "persona_responsable"]):
        enviar_datos("proyectos/", payload)

#funcion para subir Tarea
def subir_tarea():
    print("\n--- SUBIR NUEVA TAREA ---")
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")
    estado = input("Estado (PENDIENTE, EN PROGRESO, COMPLETADA): ").upper()
    proyecto = input("ID del proyecto: ")
    asignado_a = input("ID de la persona asignada: ")

    if estado not in ["PENDIENTE", "EN PROGRESO", "COMPLETADA"]:
        print("Estado inválido.")
        return

    payload = {
        "titulo": titulo,
        "descripcion": descripcion,
        "estado": estado,
        "proyecto": proyecto,
        "asignado_a": asignado_a
    }

    if validar_campos(payload, ["titulo", "descripcion", "estado", "proyecto", "asignado_a"]):
        enviar_datos("tareas/", payload)

#funcion para subir Comentario
def subir_comentario():
    print("\n--- SUBIR NUEVO COMENTARIO ---")
    contenido = input("Contenido: ")
    tarea = input("ID de la tarea: ")
    autor = input("ID del autor: ")

    payload = {
        "contenido": contenido,
        "tarea": tarea,
        "autor": autor
    }

    if validar_campos(payload, ["contenido", "tarea", "autor"]):
        enviar_datos("comentarios/", payload)

#funcion para subir Documentos
def subir_documento():
    print("\n--- SUBIR NUEVO DOCUMENTO / ENLACE ---")
    nombre = input("Nombre del documento o recurso: ")
    enlace = input("Enlace al documento (opcional, URL): ") 
    tarea = input("ID de la tarea: ") 
    descripcion = input("Descripción (opcional): ")
    tipo = input("Tipo (DOCUMENTO / ENLACE): ").upper()
    autor = input("ID del autor: ")

    payload = {
        "nombre": nombre,
        "enlace": enlace if enlace else None,
        "descripcion": descripcion if descripcion else None,
        "tarea": tarea, 
        "tipo": tipo,
        "autor":autor
    }

    # Validar los campos obligatorios
    if validar_campos(payload, ["nombre", "tarea"]):
        enviar_datos("documentos/", payload)


def enviar_datos(endpoint, payload):
    url = BASE_URL + endpoint
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            print("Datos subidos exitosamente.")
        else:
            print("Error al subir los datos:", response.status_code, response.json())
    except Exception as e:
        print("Error al conectarse a la API:", str(e))
    finally:
        menu_subir_datos() 

# Iniciar el programa
if __name__ == "__main__":
    if verificar_api(): 
        menu_principal()
    else:
        print("No se puede conectar a la API (Recuerda tener iniciado el proyecto).\nEl programa se cerrará.")
        sys.exit(1)
