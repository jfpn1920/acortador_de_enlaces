import random
import string
enlaces = {}
#----------------------------------------#
#--|menu_pricipal_acortador_de_enlaces|--#
#----------------------------------------#
def menu_principal():
    while True:
        print("\n========================================")
        print("         ACORTADOR DE ENLACES")
        print("========================================")
        print("1. Acortar enlace")
        print("2. Listar enlaces")
        print("3. Buscar enlace")
        print("4. Abrir enlace")
        print("5. Eliminar enlace")
        print("6. Mostrar estadísticas")
        print("7. Salir")
        print("========================================")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            acortar_enlace()
        elif opcion == "2":
            listar_enlaces()
        elif opcion == "3":
            buscar_enlace()
        elif opcion == "4":
            abrir_enlace()
        elif opcion == "5":
            eliminar_enlace()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            salir()
        else:
            print("\nOpción inválida. Intente nuevamente.")
#--------------------------#
#--|generar_codigo_corto|--#
#--------------------------#
def generar_codigo():
    caracteres = string.ascii_letters + string.digits
    while True:
        codigo = ""
        for i in range(6):
            codigo += random.choice(caracteres)
        if codigo not in enlaces:
            return codigo
#--------------------#
#--|acortar_enlace|--#
#--------------------#
def acortar_enlace():
    print("\n================================")
    print("       ACORTAR ENLACE")
    print("================================")
    url = input("Ingrese la URL que desea acortar: ").strip()
    if url == "":
        print("\nLa URL no puede estar vacía.")
        return
    codigo = generar_codigo()
    enlaces[codigo] = url
    print("\nEnlace acortado correctamente.")
    print("URL original:", url)
    print("URL corta: https://acortador.local/" + codigo)
#--------------------#
#--|listar_enlaces|--#
#--------------------#
def listar_enlaces():
    print("\n================================")
    print("       LISTA DE ENLACES")
    print("================================")
    if len(enlaces) == 0:
        print("No hay enlaces registrados.")
        return
    contador = 1
    for codigo, url in enlaces.items():
        print("\nEnlace", contador)
        print("Código:", codigo)
        print("URL corta: https://acortador.local/" + codigo)
        print("URL original:", url)
        contador += 1
#-------------------#
#--|buscar_enlace|--#
#-------------------#
def buscar_enlace():
    print("\n================================")
    print("        BUSCAR ENLACE")
    print("================================")
    if len(enlaces) == 0:
        print("No hay enlaces registrados.")
        return
    codigo = input("Ingrese el código del enlace: ").strip()
    if codigo in enlaces:
        print("\nEnlace encontrado.")
        print("Código:", codigo)
        print("URL corta: https://acortador.local/" + codigo)
        print("URL original:", enlaces[codigo])
    else:
        print("\nNo se encontró ningún enlace con ese código.")
#------------------#
#--|abrir_enlace|--#
#------------------#
def abrir_enlace():
    print("\n================================")
    print("         ABRIR ENLACE")
    print("================================")
    if len(enlaces) == 0:
        print("No hay enlaces registrados.")
        return
    codigo = input("Ingrese el código del enlace: ").strip()
    if codigo in enlaces:
        print("\nRedireccionando...")
        print("URL original:")
        print(enlaces[codigo])
    else:
        print("\nEl enlace no existe.")
#---------------------#
#--|eliminar_enlace|--#
#---------------------#
def eliminar_enlace():
    print("\n================================")
    print("        ELIMINAR ENLACE")
    print("================================")
    if len(enlaces) == 0:
        print("No hay enlaces registrados.")
        return
    codigo = input("Ingrese el código del enlace: ").strip()
    if codigo in enlaces:
        print("\nEnlace encontrado.")
        print("URL:", enlaces[codigo])
        confirmar = input("¿Desea eliminarlo? (s/n): ").lower()
        if confirmar == "s":
            del enlaces[codigo]
            print("\nEnlace eliminado correctamente.")
        else:
            print("\nOperación cancelada.")
    else:
        print("\nNo se encontró ningún enlace con ese código.")
#--------------------------#
#--|mostrar_estadísticas|--#
#--------------------------#
def mostrar_estadisticas():
    print("\n================================")
    print("          ESTADÍSTICAS")
    print("================================")
    total = len(enlaces)
    print("Total de enlaces registrados:", total)
    if total == 0:
        print("No hay enlaces para mostrar.")
    else:
        print("El acortador tiene", total, "enlace(s) almacenado(s).")
#------------------------------#
#--|salir_del_menu_principal|--#
#------------------------------#
def salir():
    print("\n================================")
    print("       SALIR DEL PROGRAMA")
    print("================================")
    print("Gracias por utilizar el")
    print("Acortador de Enlaces.")
    return False
menu_principal()