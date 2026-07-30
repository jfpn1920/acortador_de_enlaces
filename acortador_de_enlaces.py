import random
import string
enlaces = {}
#----------------------------------------#
#--|menu_pricipal_acortador_de_enlaces|--#
#----------------------------------------#
def menu_principal():
    while True:
        print("menu pricipal acortador de enlaces")
        print("1) acortar enlace")
        print("2) listar enlaces")
        print("3) buscar enlace")
        print("4) abrir enlace")
        print("5) eliminar enlace")
        print("6) mostrar estadísticas")
        print("7) salir")
        opcion = input("seleccione una opción: ").strip()
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
            print("opción inválida, intente nuevamente.")
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
    print("acortar enlace")
    url = input("ingrese la url que desea acortar: ").strip()
    if url == "":
        print("la url no puede estar vacía.")
        return
    codigo = generar_codigo()
    enlaces[codigo] = url
    print("enlace acortado correctamente.")
    print("url original:", url)
    print("url corta: https://acortador.local/" + codigo)
#--------------------#
#--|listar_enlaces|--#
#--------------------#
def listar_enlaces():
    print("listar enlaces")
    if len(enlaces) == 0:
        print("no hay enlaces registrados.")
        return
    contador = 1
    for codigo, url in enlaces.items():
        print("enlace", contador)
        print("código:", codigo)
        print("url corta: https://acortador.local/" + codigo)
        print("url original:", url)
        contador += 1
#-------------------#
#--|buscar_enlace|--#
#-------------------#
def buscar_enlace():
    print("buscar enlace")
    if len(enlaces) == 0:
        print("no hay enlaces registrados.")
        return
    codigo = input("ingrese el código del enlace: ").strip()
    if codigo in enlaces:
        print("enlace encontrado.")
        print("código:", codigo)
        print("url corta: https://acortador.local/" + codigo)
        print("url original:", enlaces[codigo])
    else:
        print("no se encontró ningún enlace con ese código.")
#------------------#
#--|abrir_enlace|--#
#------------------#
def abrir_enlace():
    print("abrir enlace")
    if len(enlaces) == 0:
        print("no hay enlaces registrados.")
        return
    codigo = input("ingrese el código del enlace: ").strip()
    if codigo in enlaces:
        print("redireccionando...")
        print("url original:")
        print(enlaces[codigo])
    else:
        print("el enlace no existe.")
#---------------------#
#--|eliminar_enlace|--#
#---------------------#
def eliminar_enlace():
    print("eliminar enlace")
    if len(enlaces) == 0:
        print("no hay enlaces registrados.")
        return
    codigo = input("ingrese el código del enlace: ").strip()
    if codigo in enlaces:
        print("enlace encontrado.")
        print("url:", enlaces[codigo])
        confirmar = input("¿desea eliminarlo? (s/n): ").lower()
        if confirmar == "s":
            del enlaces[codigo]
            print("enlace eliminado correctamente.")
        else:
            print("operación cancelada.")
    else:
        print("no se encontró ningún enlace con ese código.")
#--------------------------#
#--|mostrar_estadísticas|--#
#--------------------------#
def mostrar_estadisticas():
    print("mostrar estadísticas")
    total = len(enlaces)
    print("total de enlaces registrados:", total)
    if total == 0:
        print("no hay enlaces para mostrar.")
    else:
        print("el acortador tiene", total, "enlace(s) almacenado(s).")
#------------------------------#
#--|salir_del_menu_principal|--#
#------------------------------#
def salir():
    print("salir del menu principal")
    print("gracias por utilizar el acortador de Enlaces.")
    return False
menu_principal()