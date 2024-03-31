from rich.console import Console
from colorama import Fore, Style, init as colorama_init
console = Console()
colorama_init(autoreset=True)

class Maqueta:
    def __init__(self, nombre, filas, columnas, items, ListaLaberintos, entrada):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.items = items
        self.laberintos = ListaLaberintos
        self.entrada = entrada
        self.siguiente = None

class ListaEnlazada_Maquetas:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas, items, ListaLaberintos, entrada):
        nuevo_nodo = Maqueta(nombre,filas, columnas, items, ListaLaberintos, entrada)
        if self.esta_vacia() or nombre.lower()< self.primero.nombre.lower():
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None and actual.siguiente.nombre.lower()< nombre.lower():
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            
    def get(self):
        if not self.esta_vacia():
            maqueta_actual = self.primero
            contador =0 
            while maqueta_actual is not None:
                contador+=1
                print(Fore.MAGENTA+Style.BRIGHT+"\nMaqueta "+str(contador))
                print(Fore.MAGENTA+Style.BRIGHT+"Nombre: "+maqueta_actual.nombre)
                maqueta_actual = maqueta_actual.siguiente
        else:
            console.print("\nTODAVIA NO HAY MAQUETAS CARGADAS EN EL SISTEMA", style="italic #ff1a1a")

    def disponibilidad(self, nombre):
        if not self.esta_vacia():
            maqueta_actual = self.primero
            while maqueta_actual is not None:
                if maqueta_actual.nombre == nombre:
                    return maqueta_actual
                else:
                    maqueta_actual = maqueta_actual.siguiente
        else:
            return None