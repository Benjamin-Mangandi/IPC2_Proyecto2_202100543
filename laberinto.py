class Bloque:
    def __init__(self, estructura):
        self.estructura = estructura
        self.siguiente = None

class ListaEnlazada_Laberintos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, estructura):
        nuevo_nodo = Bloque(estructura)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            
    def get(self, indice):
        if not self.esta_vacia():
            bloque_actual = self.primero
            conteo = 0
            while bloque_actual is not None:
                if indice == conteo:
                    return bloque_actual.estructura
                conteo+=1
                bloque_actual=bloque_actual.siguiente
        else:
            print("La lista está vacia")
