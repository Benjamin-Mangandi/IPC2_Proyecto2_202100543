from graphviz import Graph

def crear_maqueta(maqueta_deseada):
    maqueta = Graph('G', filename='maqueta_'+maqueta_deseada.nombre+'.gv', engine='neato')
    
    maqueta.attr(overlap='false', splines='false', bgcolor='beige')

    maqueta.attr(label="Federaciom, S.A.\n"+'Maqueta: '+maqueta_deseada.nombre, fontsize='15', labelloc='t')
    
    maqueta.attr('node', shape='square', width='0.35', height='0.35', fixedsize='true', fontsize='0')

    indice =0
    
    for i in range(int(maqueta_deseada.filas)):
        for j in range(int(maqueta_deseada.columnas)):
            estructura_bloque = maqueta_deseada.laberintos.get(indice)
            indice+=1
            if str(estructura_bloque) == "*":
                color = 'white'
            elif str(estructura_bloque) == "-":
                color = 'black'
            maqueta.node(f'{i+1}{j+1}', style='filled', fillcolor=color)
    
    espaciado = 0.4
    for i in range(int(maqueta_deseada.filas)):
        for j in range(int(maqueta_deseada.columnas)):
            pos_x = j * espaciado
            pos_y = -i * espaciado
            maqueta.node(f'{i+1}{j+1}', pos=f'{pos_x},{pos_y}!')
    
    maqueta.view()