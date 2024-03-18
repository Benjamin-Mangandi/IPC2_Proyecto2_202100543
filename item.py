class Item:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class ListaEnlazada_Items:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, nombre, filas, columnas):
        nuevo_nodo = Item(nombre,filas, columnas)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
    
    def get(self, fila, columna):
        if not self.esta_vacia():
            item_actual = self.primero
            while item_actual is not None:
                if item_actual.fila == fila and item_actual.columna == columna:
                    return item_actual
                item_actual=item_actual.siguiente
            return None
        else:
            return None
    
    def imprimir(self):
        if not self.esta_vacia():
            item_actual = self.primero
            while item_actual is not None:
                print(item_actual.nombre)
                item_actual=item_actual.siguiente
        else:
            return None
    
    def copiar(self,ListaOriginal):
        lista_nueva = ListaEnlazada_Items()
        Item_actual = ListaOriginal.primero
        while Item_actual:
            lista_nueva.add(Item_actual.nombre, Item_actual.fila, Item_actual.columna)
            Item_actual = Item_actual.siguiente
        return lista_nueva
            
