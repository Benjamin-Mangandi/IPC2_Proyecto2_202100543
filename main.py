import os
import subprocess
import xml.etree.ElementTree as ET
from colorama import Fore, Style, init as colorama_init
from rich.console import Console
from rich.progress import track
from maqueta import ListaEnlazada_Maquetas
from item import ListaEnlazada_Items
from laberinto import ListaEnlazada_Laberintos
from graphics import crear_maqueta, crear_camino
from entrada import Entrada
import time

colorama_init(autoreset=True)
console = Console()
Maquetas_cargadas = ListaEnlazada_Maquetas()

def save_data(raiz):
    for _ in track(range(1), description=Fore.BLUE+Style.BRIGHT+"Procesando archivo..."):
        time.sleep(1)
    global Pisos_cargados
    maquetas = raiz.find("maquetas")
    for maqueta in maquetas.findall('maqueta'):
        items = ListaEnlazada_Items()
        nombre_maqueta = maqueta.find('nombre').text.strip()
        filas = maqueta.find('filas').text.strip()
        columnas = maqueta.find('columnas').text.strip()
        aux_estructuras = maqueta.find('estructura').text.strip()
        aux_estructuras = aux_estructuras.replace("\n", "")
        estructuras = aux_estructuras.replace(" ", "")
        print(estructuras)
        nuevo_laberinto = ListaEnlazada_Laberintos()
        fila = 0
        columna = 0
        for estructura in estructuras:
            nueva_estructura = estructura
            if estructura == "*":
                nuevo_laberinto.add(nueva_estructura, True, fila, columna)
                columna+=1
            if estructura == "-":
                nuevo_laberinto.add(nueva_estructura, False, fila, columna)
                columna+=1
            if int(columna) == int(columnas):
                columna = 0
                fila+=1
        for entrada in maqueta.findall('entrada'):
            filas_entrada = entrada.find('fila').text.strip()
            columnas_entrada = entrada.find('columna').text.strip()
        nueva_entrada = Entrada(filas_entrada, columnas_entrada)
        objetivos = maqueta.find("objetivos")
        for objetivo in objetivos:
            nombre_objetivo = objetivo.find('nombre').text.strip()
            fila_objetivo = objetivo.find('fila').text.strip()
            columna_objetivo = objetivo.find('columna').text.strip()
            items.add(nombre_objetivo, fila_objetivo, columna_objetivo)
        Maquetas_cargadas.add(nombre_maqueta, filas, columnas, items, nuevo_laberinto, nueva_entrada)
    print(Fore.BLUE+Style.BRIGHT+"\nARCHIVO DE MAQUETAS CARGADO CORRECTAMENTE")

def submenu():
    respuesta_usuario = 0
    while respuesta_usuario != str(3):
        console.print("\n[#ffcc00 bold]1. Ver Listado de Maquetas",style="#ffcc00 bold") #SUB MENU
        console.print("[#ffcc00 bold]2. Ver Graficamente una Maqueta", style="#ffcc00 bold")
        console.print("[italic #ffcc00 bold]3. Regresar al menú principal", style="italic #ffcc00 bold")
        respuesta_usuario = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\nOpción: ")
        if respuesta_usuario == str(1):
            Maquetas_cargadas.get()
        if respuesta_usuario == str(2):
            if Maquetas_cargadas.esta_vacia() is False:
                nombre_maqueta_deseada = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\nIngrese el nombre de la maqueta deseada: ")
                maqueta_deseada = Maquetas_cargadas.disponibilidad(nombre_maqueta_deseada)
                if maqueta_deseada is not None:
                    for _ in track(range(1), description=Fore.BLUE+Style.BRIGHT+"Procesando archivo..."):
                        time.sleep(1)
                    crear_maqueta(maqueta_deseada)
                else:
                    console.print("\nLA MAQUETA NO EXISTE EN EL SISTEMA.Intentelo de Nuevo.", style="italic #ff1a1a")
            else:
                console.print("\nTODAVIA NO HAY MAQUETAS CARGADAS EN EL SISTEMA", style="italic #ff1a1a")
        if respuesta_usuario == str(3):
            return

def menu():
    global Maquetas_cargadas
    console.print("\n"+"-"*20+"Bienvenido"+"-"*20, style="italic #00ffff bold")
    console.print("\nPor favor seleccione una opción", style="italic #00ffff bold")
    respuesta_usuario = 0
    while respuesta_usuario != str(6):
        console.print("\n[#ffcc00 bold]1. Cargar archivo XML" , style="#ffcc00 bold") #MENU INICIAL
        console.print("[#ffcc00 bold]2. Reiniciar Datos Cargados Previamente" , style="#ffcc00 bold")
        console.print("[#ffcc00 bold]3. Gestionar Maquetas Cargadas", style="#ffcc00 bold")
        console.print("[#ffcc00 bold]4. Resolver Maquetas Cargadas", style="#ffcc00 bold")
        console.print("[#ffcc00 bold]5. Ayuda (Documentación)", style="#ffcc00 bold")
        console.print("[italic #ffcc00 bold]6. Salir de la aplicación", style="italic #ffcc00 bold")
        respuesta_usuario = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\nOpción: ")
        if respuesta_usuario == str(1):
            nombre_archivo = input("\nIngrese el nombre del archivo XML en el escritorio: ")
            ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
            ruta_xml = os.path.join(ruta_escritorio, nombre_archivo)
            if os.path.exists(ruta_xml):
                tree = ET.parse(ruta_xml)
                raiz = tree.getroot()
                save_data(raiz)
            else:
                console.print(f"\nEl archivo {nombre_archivo} no existe en el escritorio.\n",style="italic #ff1a1a")
        if respuesta_usuario == str(2):
            global Maquetas_cargadas
            Maquetas_cargadas = ListaEnlazada_Maquetas()
            console.print("\nLISTA DE MAQUETAS REINICIADA CON EXITO", style="italic #ff1a1a bold")
        if respuesta_usuario == str(3):
            submenu()
        if respuesta_usuario == str(4):
            if Maquetas_cargadas.esta_vacia() is False:
                nombre_maqueta_deseada = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\nIngrese el nombre de la maqueta deseada: ")
                maqueta_deseada = Maquetas_cargadas.disponibilidad(nombre_maqueta_deseada)
                if maqueta_deseada is not None:
                    for _ in track(range(1), description=Fore.BLUE+Style.BRIGHT+"Procesando archivo..."):
                        time.sleep(1)
                    laberinto_solucion= maqueta_deseada.laberintos.movement(maqueta_deseada.laberintos,maqueta_deseada.entrada, maqueta_deseada.items)
                    crear_camino(maqueta_deseada, laberinto_solucion)
                else:
                    console.print("\nLA MAQUETA NO EXISTE EN EL SISTEMA.Intentelo de Nuevo.", style="italic #ff1a1a")
            else:
                console.print("\nTODAVIA NO HAY MAQUETAS CARGADAS EN EL SISTEMA", style="italic #ff1a1a")
        if respuesta_usuario == str(5):
            console.print("\nHAROLD BENJAMIN OXLAJ MANGANDI", style="italic #00cc00 bold")
            console.print("[italic #00e600 bold]202100543")
            console.print("https://github.com/Benjamin-Mangandi/IPC2_Proyecto2_202100543.git")
            try:
                nombre_del_archivo = '[IPC2]202100543_EnsayoProyecto2.pdf'
                subprocess.run(['start', nombre_del_archivo], shell=True)
            except FileNotFoundError:
                print("El archivo no se encontró en el escritorio.")
            except subprocess.CalledProcessError:
                print("No se pudo abrir el archivo por alguna razón.")

menu()