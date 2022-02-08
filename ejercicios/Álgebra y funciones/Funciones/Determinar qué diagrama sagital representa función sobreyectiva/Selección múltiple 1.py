{"cantidad_opciones":1, "cantidad_disponible":50}

#===============================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras
def dominio_usado_con_uno_extra():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    par_de_puntos_unidos = []
    puntos_dominio_usados = []
    puntos_codominio_usados = []
    cantidad_de_flechas = len(puntos_dominio)+1
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or (len(puntos_dominio_usados)<len(puntos_dominio) and punto_dominio in puntos_dominio_usados):
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"


def dominio_sin_usar_por_completo_sin_repeticion():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    par_de_puntos_unidos = []
    puntos_dominio_usados = []
    puntos_codominio_usados = []
    cantidad_de_flechas = randrange(1, len(puntos_dominio))
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or punto_dominio in puntos_dominio_usados:
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"


def dominio_sin_usar_por_completo_con_repeticion():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    punto_dominio_que_no_se_usara = choice(puntos_dominio)
    par_de_puntos_unidos = []
    puntos_dominio_usados = []
    puntos_codominio_usados = []
    cantidad_de_flechas = len(puntos_dominio)
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or punto_dominio==punto_dominio_que_no_se_usara:
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"


def funcion_no_sobre_no_iny():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    punto_1_dominio_que_comparte_una_imagen = choice(puntos_dominio)
    punto_2_dominio_que_comparte_una_imagen = choice(puntos_dominio)
    while punto_1_dominio_que_comparte_una_imagen==punto_2_dominio_que_comparte_una_imagen:
        punto_2_dominio_que_comparte_una_imagen = choice(puntos_dominio)
    punto_codominio_que_recibe_dos = choice(puntos_codominio)
    punto_codominio_que_no_recibe = choice(puntos_codominio)
    while punto_codominio_que_recibe_dos==punto_codominio_que_no_recibe:
        punto_codominio_que_no_recibe = choice(puntos_codominio)
    flechas += fr"\draw [->] ({punto_1_dominio_que_comparte_una_imagen}.east) to ({punto_codominio_que_recibe_dos}.west);"+"\n"
    flechas += fr"\draw [->] ({punto_2_dominio_que_comparte_una_imagen}.east) to ({punto_codominio_que_recibe_dos}.west);"+"\n"
    par_de_puntos_unidos = [[punto_1_dominio_que_comparte_una_imagen,punto_codominio_que_recibe_dos], [punto_2_dominio_que_comparte_una_imagen,punto_codominio_que_recibe_dos]]
    puntos_dominio_usados = [punto_1_dominio_que_comparte_una_imagen, punto_2_dominio_que_comparte_una_imagen]
    puntos_codominio_usados = []
    cantidad_de_flechas = len(puntos_dominio)-2
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or punto_dominio in puntos_dominio_usados or punto_codominio==punto_codominio_que_no_recibe:
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"


def funcion_si_sobre_no_iny():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,5)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,len(puntos_dominio)-1):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    par_de_puntos_unidos = []
    puntos_dominio_usados = []
    puntos_codominio_usados = []
    cantidad_de_flechas = len(puntos_dominio)
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or punto_dominio in puntos_dominio_usados or (len(puntos_codominio_usados)<len(puntos_codominio) and punto_codominio in puntos_codominio_usados):
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"


def funcion_no_sobre_si_iny():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,4)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,len(puntos_dominio)+choice([1,2])):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    par_de_puntos_unidos = []
    puntos_dominio_usados = []
    puntos_codominio_usados = []
    cantidad_de_flechas = len(puntos_dominio)
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or punto_dominio in puntos_dominio_usados or punto_codominio in puntos_codominio_usados:
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"


def funcion_bi():
    puntos_dominio = []
    lista_letras = ["A", "B", "C", "D", "E", "F"]
    numeros_en_dominio = []
    for i in range(0,randrange(2,4)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_dominio:
            numero_provisional = randrange(-9,10)
        numeros_en_dominio.append(numero_provisional)
    numeros_en_dominio = sorted(numeros_en_dominio)
    elipse_dominio = fr"\node (A1) at (0,0) {{${numeros_en_dominio[0]}$}}; \filldraw (A1.east) circle (2pt);"+"\n"
    puntos_dominio.append("A1")
    espacio_vertical = -1
    for preimagen in numeros_en_dominio[1:]:
        letra = lista_letras[numeros_en_dominio.index(preimagen)]
        elipse_dominio += fr"\node ({letra}1) at (0,{espacio_vertical}) {{${preimagen}$}}; \filldraw ({letra}1.east) circle (2pt);"+"\n"
        puntos_dominio.append(lista_letras[numeros_en_dominio.index(preimagen)]+"1")
        espacio_vertical -= 1
    elipse_dominio +=r"\node[fit="
    for punto in puntos_dominio:
        elipse_dominio += "("+punto+")"
    elipse_dominio += ", ellipse, draw]{};"


    puntos_codominio = []
    numeros_en_codominio = []
    for i in range(0,len(puntos_dominio)):
        numero_provisional = randrange(-9,10)
        while numero_provisional in numeros_en_codominio:
            numero_provisional = randrange(-9,10)
        numeros_en_codominio.append(numero_provisional)
    numeros_en_codominio = sorted(numeros_en_codominio)
    puntos_codominio.append("A2")
    elipse_codominio = "\n"+fr"\node (A2) at (3,0) {{${numeros_en_codominio[0]}$}}; \filldraw (A2.west) circle (2pt);"+"\n"
    espacio_vertical = -1
    for imagen in numeros_en_codominio[1:]:
        letra = lista_letras[numeros_en_codominio.index(imagen)]
        elipse_codominio += fr"\node ({letra}2) at (3,{espacio_vertical}) {{${imagen}$}}; \filldraw ({letra}2.west) circle (2pt);"+"\n"
        puntos_codominio.append(lista_letras[numeros_en_codominio.index(imagen)]+"2")
        espacio_vertical -= 1
    elipse_codominio +=r"\node[fit="
    for punto in puntos_codominio:
        elipse_codominio += "("+punto+")"
    elipse_codominio += ", ellipse, draw]{};"

    flechas = "\n"
    par_de_puntos_unidos = []
    puntos_dominio_usados = []
    puntos_codominio_usados = []
    cantidad_de_flechas = len(puntos_dominio)
    for i in range(0, cantidad_de_flechas):
        punto_dominio = choice(puntos_dominio)
        punto_codominio = choice(puntos_codominio)
        while [punto_dominio, punto_codominio] in par_de_puntos_unidos or punto_dominio in puntos_dominio_usados or punto_codominio in puntos_codominio_usados:
            punto_dominio = choice(puntos_dominio)
            punto_codominio = choice(puntos_codominio)
        puntos_dominio_usados.append(punto_dominio)
        puntos_codominio_usados.append(punto_codominio)
        par_de_puntos_unidos.append([punto_dominio, punto_codominio])
        flechas += fr"\draw [->] ({punto_dominio}.east) to ({punto_codominio}.west);"+"\n"

    return r"\begin{tabular}{l} \begin{tikzpicture} [scale=0.5]"+"\n"+elipse_dominio+elipse_codominio+flechas+"\n"+r"\end{tikzpicture} \end{tabular}"



#===============================================Aquí va el número del ejercicio y el enunciado.
enunciado = f"¿En cuál de los siguientes diagramas sagitales se representa una función {choice(['sobreyectiva', 'epiyectiva'])}?"
#===================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.
contenido_correcto = choice([funcion_si_sobre_no_iny(), funcion_bi()])
contenido_2 = funcion_no_sobre_no_iny()
contenido_3 = funcion_no_sobre_si_iny()
contenido_4 = dominio_usado_con_uno_extra()
contenido_5 = choice([dominio_usado_con_uno_extra(), dominio_sin_usar_por_completo_sin_repeticion(), dominio_sin_usar_por_completo_con_repeticion()])


enunciado_oculto = contenido_correcto











