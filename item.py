class Item:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas

class ListaEnlazada_Items:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas):
        nuevo_nodo = Item(nombre,filas, columnas)
        if self.esta_vacia() or nombre.lower()< self.primero.nombre.lower():
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None and actual.siguiente.nombre.lower()< nombre.lower():
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def get(self, fila, columna):
        if not self.esta_vacia():
            item_actual = self.primero
            while item_actual is not None:
                if item_actual.filas == fila and item_actual.columnas == columna:
                    return item_actual
                item_actual=item_actual.siguiente
            return None
        else:
            return None
            
