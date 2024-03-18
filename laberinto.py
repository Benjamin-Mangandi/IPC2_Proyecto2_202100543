class Bloque:
    def __init__(self, estructura,Boleano, fila, columna):
        self.fila = fila
        self.columna = columna
        self.estructura = estructura
        self.esPared = Boleano
        self.visitado = False
        self.siguiente = None

class ListaEnlazada_Laberintos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def add(self, estructura, Boleano, fila, columna):
        nuevo_nodo = Bloque(estructura, Boleano, fila, columna)
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
            return None
    
    def get_coordenadas(self,fila, columna):
        if not self.esta_vacia():
            bloque_actual = self.primero
            while bloque_actual is not None:
                if str(bloque_actual.fila) == str(fila) and str(bloque_actual.columna) == str(columna) :
                    return bloque_actual
                bloque_actual=bloque_actual.siguiente
        else:
            return None
        
    def copiar(self,ListaOriginal):
        lista_nueva = ListaEnlazada_Laberintos()
        bloque_actual = ListaOriginal.primero
        while bloque_actual:
            lista_nueva.add(bloque_actual.estructura, bloque_actual.esPared, bloque_actual.fila, bloque_actual.columna)
            bloque_actual = bloque_actual.siguiente
        return lista_nueva
    
    def modificar(self, fila, columna):
        if not self.esta_vacia():
            bloque_actual = self.primero
            while bloque_actual is not None:
                if str(bloque_actual.fila) == str(fila) and str(bloque_actual.columna) == str(columna) :
                    bloque_actual.estructura = "#"
                    return
                bloque_actual=bloque_actual.siguiente
        else:
            return None
    
    def movement(self, ListaOriginal, entrada, objetivos):
        if not self.esta_vacia():
            aux_laberinto = self.copiar(ListaOriginal)
            aux2_laberinto = self.copiar(ListaOriginal)
            objetivo_actual = objetivos.primero
            posicion_actual = aux_laberinto.get_coordenadas(entrada.fila, entrada.columna)
            while objetivo_actual is not None:
                bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, int(posicion_actual.columna))
                bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, int(posicion_actual.columna))
                bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if int(objetivo_actual.fila) == int(posicion_actual.fila) and int(objetivo_actual.columna) == int(posicion_actual.columna):
                    objetivo_actual = objetivo_actual.siguiente
                    if objetivo_actual is None:
                        return
                if int(objetivo_actual.fila) > int(posicion_actual.fila):
                    if bloque_abajo is not None and bloque_abajo.esPared is False:
                        posicion_actual = aux_laberinto.get_coordenadas(bloque_abajo.fila, bloque_abajo.columna)
                        print("Para abajo")
                        aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
                        bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
                        bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
                        bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                        bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if int(objetivo_actual.columna) > int(posicion_actual.columna):
                    if bloque_derecha is not None and bloque_derecha.esPared is False:
                        posicion_actual = aux_laberinto.get_coordenadas(bloque_derecha.fila, bloque_derecha.columna)
                        print("Para derecha")
                        aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
                        bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
                        bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
                        bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                        bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if int(objetivo_actual.fila) < int(posicion_actual.fila):
                    if bloque_arriba is not None and bloque_arriba.esPared is False:
                        posicion_actual = aux_laberinto.get_coordenadas(bloque_arriba.fila, bloque_arriba.columna)
                        print("Para arriba")
                        aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
                        bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
                        bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
                        bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                        bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if int(objetivo_actual.columna) < int(posicion_actual.columna):
                    if bloque_izquierda is not None and bloque_izquierda.esPared is False:
                        posicion_actual = aux_laberinto.get_coordenadas(bloque_izquierda.fila, bloque_izquierda.columna)
                        print("Para izquierda")
                        aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
                        bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
                        bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
                        bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                        bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if bloque_derecha is not None and bloque_arriba is not None \
                      and bloque_izquierda is not None:
                    if bloque_derecha.esPared and bloque_arriba.esPared and bloque_izquierda.esPared:
                        return
        else:
            return None
