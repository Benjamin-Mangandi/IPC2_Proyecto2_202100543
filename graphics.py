from graphviz import Graph

def crear_maqueta(maqueta_deseada):
    maqueta = Graph('G', filename='maqueta_'+maqueta_deseada.nombre+'.gv', engine='neato')
    
    maqueta.attr(overlap='false', splines='false', bgcolor='orange')

    maqueta.attr(label="Escuela de Sistemas\n"+'Maqueta: '+maqueta_deseada.nombre, fontsize='15', labelloc='t')
    
    maqueta.attr('node', shape='square', width='0.35', height='0.35', fixedsize='true', fontsize='10')

    indice = 0
    
    for i in range(int(maqueta_deseada.filas)):
        for j in range(int(maqueta_deseada.columnas)):
            estructura_bloque = maqueta_deseada.laberintos.get(indice)
            item = maqueta_deseada.items.get(str(i),str(j))
            indice+=1
            if str(estructura_bloque) == "*":
                color = 'black'
            elif str(estructura_bloque) == "-":
                color = 'white'
            if maqueta_deseada.entrada.fila == str(i) \
            and maqueta_deseada.entrada.columna == str(j):
                color = 'green'
            if item is not None:
                maqueta.node(f'{i}{j}', label=item.nombre ,style='filled', fillcolor=color)
            else:
                maqueta.node(f'{i}{j}', label='',style='filled', fillcolor=color)
    
    espaciado = 0.38
    for i in range(int(maqueta_deseada.filas)):
        for j in range(int(maqueta_deseada.columnas)):
            pos_x = j * espaciado
            pos_y = -i * espaciado
            maqueta.node(f'{i}{j}',pos=f'{pos_x},{pos_y}!')
    
    maqueta.view()

def crear_camino(maqueta_deseada, laberinto):
    maqueta = Graph('G', filename='maqueta_'+maqueta_deseada.nombre+'_solucion'+'.gv', engine='neato')
    
    maqueta.attr(overlap='false', splines='false', bgcolor='orange')

    maqueta.attr(label="Escuela de Sistemas\n"+'Maqueta: '+maqueta_deseada.nombre+"\n"+"Solución:", fontsize='15', labelloc='t')
    
    maqueta.attr('node', shape='square', width='0.35', height='0.35', fixedsize='true', fontsize='10')

    indice = 0
    
    for i in range(int(maqueta_deseada.filas)):
        for j in range(int(maqueta_deseada.columnas)):
            estructura_bloque = laberinto.get(indice)
            item = maqueta_deseada.items.get(str(i),str(j))
            indice+=1
            if str(estructura_bloque) == "*":
                color = 'black'
            elif str(estructura_bloque) == "-":
                color = 'white'
            elif str(estructura_bloque) == "#":
                color = 'cyan'
            if maqueta_deseada.entrada.fila == str(i) \
            and maqueta_deseada.entrada.columna == str(j):
                color = 'green'
            if item is not None:
                maqueta.node(f'{i}{j}', label=item.nombre ,style='filled', fillcolor=color)
            else:
                maqueta.node(f'{i}{j}', label='',style='filled', fillcolor=color)
    
    espaciado = 0.38
    for i in range(int(maqueta_deseada.filas)):
        for j in range(int(maqueta_deseada.columnas)):
            pos_x = j * espaciado
            pos_y = -i * espaciado
            maqueta.node(f'{i}{j}',pos=f'{pos_x},{pos_y}!')
    
    maqueta.view()