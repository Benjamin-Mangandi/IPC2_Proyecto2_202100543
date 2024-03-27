class Bloque:
    def __init__(self, estructura,Boleano, fila, columna):
        self.fila = fila
        self.columna = columna
        self.estructura = estructura
        self.esPared = Boleano
        self.visitado = False
        self.siguiente = None

bloque_abajo = None
bloque_arriba = None
bloque_derecha = None
bloque_izquierda = None
aux_laberinto = None
contador = 100
aux2_laberinto = None
posicion_actual = None
def mov_down():
    global posicion_actual
    global aux2_laberinto
    global contador
    global bloque_abajo
    global bloque_arriba
    global bloque_derecha
    global bloque_izquierda
    global aux_laberinto
    aux_laberinto.visitar(posicion_actual.fila, posicion_actual.columna)
    posicion_actual = aux_laberinto.get_coordenadas(bloque_abajo.fila, bloque_abajo.columna)
    print("Para abajo")
    aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
    bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
    bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
    bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
    bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
    contador+=1

def mov_up():
    global posicion_actual
    global aux2_laberinto
    global contador
    global bloque_abajo
    global bloque_arriba
    global bloque_derecha
    global bloque_izquierda
    global aux_laberinto
    aux_laberinto.visitar(posicion_actual.fila, posicion_actual.columna)
    posicion_actual = aux_laberinto.get_coordenadas(bloque_arriba.fila, bloque_arriba.columna)
    print("Para arriba")
    aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
    bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
    bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
    bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
    bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
    contador+=1

def mov_right():
    global posicion_actual
    global aux2_laberinto
    global contador
    global bloque_abajo
    global bloque_arriba
    global bloque_derecha
    global bloque_izquierda
    global aux_laberinto
    aux_laberinto.visitar(posicion_actual.fila, posicion_actual.columna)
    posicion_actual = aux_laberinto.get_coordenadas(bloque_derecha.fila, bloque_derecha.columna)
    print("Para derecha")
    aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
    bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
    bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
    bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
    bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
    contador+=1


def mov_left():
    global posicion_actual
    global aux2_laberinto
    global contador
    global bloque_abajo
    global bloque_arriba
    global bloque_derecha
    global bloque_izquierda
    global aux_laberinto
    aux_laberinto.visitar(posicion_actual.fila, posicion_actual.columna)
    posicion_actual = aux_laberinto.get_coordenadas(bloque_izquierda.fila, bloque_izquierda.columna)
    print("Para izquierda")
    aux2_laberinto.modificar(posicion_actual.fila, posicion_actual.columna)
    bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, posicion_actual.columna)
    bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, posicion_actual.columna)
    bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
    bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
    contador+=1

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
        
    def visitar(self, fila, columna):
        if not self.esta_vacia():
            bloque_actual = self.primero
            while bloque_actual is not None:
                if str(bloque_actual.fila) == str(fila) and str(bloque_actual.columna) == str(columna) :
                    bloque_actual.visitado = True
                    return
                bloque_actual=bloque_actual.siguiente
        else:
            return None
        
    def movement_continue(self, ListaOriginal, entrada, objetivos):
        if not self.esta_vacia():
            global bloque_abajo
            global contador
            global bloque_arriba
            global bloque_derecha
            global bloque_izquierda
            global aux_laberinto
            global posicion_actual
            global aux2_laberinto
            contador = 100
            aux_laberinto = self.copiar(ListaOriginal)
            aux2_laberinto = self.copiar(ListaOriginal)
            objetivo_actual = objetivos.primero
            posicion_actual = aux_laberinto.get_coordenadas(entrada.fila, entrada.columna)
            while contador >0 :
                bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, int(posicion_actual.columna))
                bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, int(posicion_actual.columna))
                bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if int(objetivo_actual.fila) == int(posicion_actual.fila) and int(objetivo_actual.columna) == int(posicion_actual.columna):
                    objetivo_actual = objetivo_actual.siguiente
                    if objetivo_actual is None:
                        return aux2_laberinto
                if int(objetivo_actual.columna) < int(posicion_actual.columna):
                    subcontador = 20
                    while subcontador>0:
                        if int(objetivo_actual.columna) < int(posicion_actual.columna):
                            if bloque_izquierda is not None and bloque_izquierda.esPared is False and bloque_izquierda.visitado is False:
                                mov_left()
                            elif (bloque_arriba is not None and bloque_arriba.esPared) \
                            and (bloque_abajo is not None and bloque_abajo.esPared)\
                            and (bloque_izquierda is not None and bloque_izquierda.visitado)\
                            and (bloque_derecha is not None and bloque_derecha.visitado is False and bloque_derecha.esPared is False):
                                mov_right()
                            elif (bloque_arriba is not None and bloque_arriba.esPared) \
                            and bloque_izquierda is not None and (bloque_izquierda.visitado or bloque_izquierda.esPared)\
                            and bloque_derecha is not None and (bloque_derecha.visitado or bloque_derecha.esPared)\
                            and bloque_abajo is not None and bloque_abajo.esPared is False and bloque_abajo.visitado is False and contador <50:
                                mov_down()
                        subcontador-=1
                if int(objetivo_actual.columna) > int(posicion_actual.columna):
                    if bloque_derecha is not None and bloque_derecha.esPared is False and bloque_derecha.visitado is False:
                        mov_right()
                    elif bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado)\
                    and (bloque_izquierda is not None and bloque_izquierda.visitado is False and bloque_izquierda.esPared is False):
                        mov_left()     
                if int(objetivo_actual.fila) > int(posicion_actual.fila):
                    if bloque_abajo is not None and bloque_abajo.esPared is False and bloque_abajo.visitado is False:
                        mov_down() 
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_izquierda is not None and bloque_izquierda.visitado\
                    and bloque_derecha is not None and (bloque_derecha.esPared or bloque_derecha.visitado)\
                    and (bloque_arriba is not None and bloque_arriba.visitado is False and bloque_arriba.esPared is False):
                        mov_up()
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_izquierda is not None and (bloque_izquierda.visitado or bloque_izquierda.esPared)\
                    and bloque_derecha is not None and (bloque_derecha.esPared or bloque_derecha.visitado)\
                    and (bloque_arriba is not None and bloque_arriba.visitado is False and bloque_arriba.esPared is False):
                        mov_up()
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_izquierda is not None and (bloque_izquierda.visitado or bloque_izquierda.esPared)\
                    and bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado is False and bloque_derecha.esPared is False) and contador<50:
                        mov_right()
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_derecha is not None and (bloque_derecha.visitado or bloque_derecha.esPared)\
                    and bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and (bloque_izquierda is not None and bloque_izquierda.visitado is False and bloque_izquierda.esPared is False) and contador<50:
                        mov_left()
                if int(objetivo_actual.fila) < int(posicion_actual.fila):
                    if bloque_arriba is not None and bloque_arriba.esPared is False and bloque_arriba.visitado is False:
                       mov_up()
                    elif bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and (bloque_izquierda is not None and bloque_izquierda.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado is False and bloque_derecha.esPared is False):
                        mov_right()
                contador-=1
            return aux2_laberinto
        else:
            return None

    def movement(self, ListaOriginal, entrada, objetivos):
        if not self.esta_vacia():
            ListaOriginal_copia = self.copiar(ListaOriginal)
            entrada_copia = entrada
            objetivos_copia = objetivos.copiar(objetivos)
            global bloque_abajo
            global contador
            global bloque_arriba
            global bloque_derecha
            global bloque_izquierda
            global aux_laberinto
            global posicion_actual
            global aux2_laberinto
            contador = 100
            aux_laberinto = self.copiar(ListaOriginal)
            aux2_laberinto = self.copiar(ListaOriginal)
            objetivo_actual = objetivos.primero
            posicion_actual = aux_laberinto.get_coordenadas(entrada.fila, entrada.columna)
            while contador >0 :
                bloque_abajo = aux_laberinto.get_coordenadas(int(posicion_actual.fila)+1, int(posicion_actual.columna))
                bloque_arriba = aux_laberinto.get_coordenadas(int(posicion_actual.fila)-1, int(posicion_actual.columna))
                bloque_derecha = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)+1)
                bloque_izquierda = aux_laberinto.get_coordenadas(int(posicion_actual.fila), int(posicion_actual.columna)-1)
                if int(objetivo_actual.fila) == int(posicion_actual.fila) and int(objetivo_actual.columna) == int(posicion_actual.columna):
                    objetivo_actual = objetivo_actual.siguiente
                    if objetivo_actual is None:
                        return aux2_laberinto
                if int(objetivo_actual.columna) < int(posicion_actual.columna):
                    if bloque_izquierda is not None and bloque_izquierda.esPared is False and bloque_izquierda.visitado is False:
                        mov_left()
                    elif (bloque_arriba is not None and bloque_arriba.esPared) \
                    and (bloque_abajo is not None and bloque_abajo.esPared)\
                    and (bloque_izquierda is not None and bloque_izquierda.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado is False and bloque_derecha.esPared is False):
                        mov_right()
                    elif (bloque_arriba is not None and bloque_arriba.esPared) \
                    and bloque_izquierda is not None and (bloque_izquierda.visitado or bloque_izquierda.esPared)\
                    and bloque_derecha is not None and (bloque_derecha.visitado or bloque_derecha.esPared)\
                    and bloque_abajo is not None and bloque_abajo.esPared is False and bloque_abajo.visitado is False and contador <50:
                        mov_down()
                if int(objetivo_actual.columna) > int(posicion_actual.columna):
                    if bloque_derecha is not None and bloque_derecha.esPared is False and bloque_derecha.visitado is False:
                        mov_right()
                    elif bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado)\
                    and (bloque_izquierda is not None and bloque_izquierda.visitado is False and bloque_izquierda.esPared is False):
                        mov_left()     
                if int(objetivo_actual.fila) > int(posicion_actual.fila):
                    if bloque_abajo is not None and bloque_abajo.esPared is False and bloque_abajo.visitado is False:
                        mov_down() 
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_izquierda is not None and bloque_izquierda.visitado\
                    and bloque_derecha is not None and (bloque_derecha.esPared or bloque_derecha.visitado)\
                    and (bloque_arriba is not None and bloque_arriba.visitado is False and bloque_arriba.esPared is False):
                        mov_up()
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_izquierda is not None and (bloque_izquierda.visitado or bloque_izquierda.esPared)\
                    and bloque_derecha is not None and (bloque_derecha.esPared or bloque_derecha.visitado)\
                    and (bloque_arriba is not None and bloque_arriba.visitado is False and bloque_arriba.esPared is False):
                        mov_up()
                    elif bloque_abajo is not None and (bloque_abajo.esPared or bloque_abajo.visitado)\
                    and bloque_izquierda is not None and (bloque_izquierda.visitado or bloque_izquierda.esPared)\
                    and bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado is False and bloque_derecha.esPared is False) and contador<50:
                        mov_right()
                if int(objetivo_actual.fila) < int(posicion_actual.fila):
                    if bloque_arriba is not None and bloque_arriba.esPared is False and bloque_arriba.visitado is False:
                       mov_up()
                    elif bloque_arriba is not None and (bloque_arriba.esPared or bloque_arriba.visitado)\
                    and (bloque_izquierda is not None and bloque_izquierda.visitado)\
                    and (bloque_derecha is not None and bloque_derecha.visitado is False and bloque_derecha.esPared is False):
                        mov_right()
                #if bloque_derecha is not None and bloque_arriba is not None \
                      #and bloque_izquierda is not None:
                    #if bloque_derecha.esPared and bloque_arriba.esPared and bloque_izquierda.esPared:
                        #return aux2_laberinto
                contador-=1
            aux3_laberinto = self.movement_continue(ListaOriginal_copia, entrada_copia, objetivos_copia)
            return aux3_laberinto
        else:
            return None
