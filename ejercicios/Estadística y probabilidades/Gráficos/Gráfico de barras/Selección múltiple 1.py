{"cantidad_opciones":3, "cantidad_disponible":50}

def tabla(eje_x, eje_y, valores, titulo=""):
    divisor = eje_y[0]
    separacion_horizontal = 1.4
    separacion_vertical = 0.5

    resultado = r"\begin{center} "+fr"""\begin{{tikzpicture}}[scale=1]
\draw [->] (0,0) -- ({len(eje_x)*separacion_horizontal+separacion_horizontal/2}, 0);
\draw [->] (0,-0.2) -- (0, {len(eje_y)*separacion_vertical+separacion_vertical/2+0.1});
\node [font=\footnotesize, rotate=90] at ({len(eje_x)*separacion_horizontal+separacion_horizontal/2+0.2}, 0) {{Juguetes}};
\node [font=\footnotesize] at (-0.2, 0) {{0}};
\node [font=\scriptsize] at (0, {len(eje_y)*separacion_vertical+separacion_vertical/2+0.3}) {{Cantidad}};
"""

    #Lineas horizontañes
    for i in range(len(eje_y)):
        resultado += fr"\draw [dashed] (0, {separacion_vertical*(i+1)}) -- ({separacion_horizontal*len(eje_x)}, {separacion_vertical*(i+1)});" + "\n"

    #Etiquetas eje y
    for i in range(len(eje_y)):
        resultado += fr"\node [font=\footnotesize] at (-0.2, {separacion_vertical*(i+1)}) {{{eje_y[i]}}};"+"\n"

    medio_ancho = 0.2
    #Barras
    for i in range(len(valores)):
        x, y = separacion_horizontal*(i+1), valores[i]*separacion_vertical/divisor
        resultado += fr"\filldraw[draw=black,fill=gray!100] plot coordinates{{ ({x-2*medio_ancho},0) ({x},0) ({x},{y}) ({x-2*medio_ancho},{y}) ({x-2*medio_ancho},0) }};"+"\n"

    #Etiquetas exe x
    for i in range(len(valores)):
        resultado += fr"\node [font=\scriptsize] at ({separacion_horizontal*(i+1)-medio_ancho}, -0.2) {{{eje_x[i]}}};"+"\n"

    return resultado + r"\end{tikzpicture} \end{center}"






class Juguete:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    def __lt__(self, other):
        return self.cantidad < other.cantidad
    def __str__(self):
        return self.nombre






#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
# Tamaño de las barras
tamaño_barras = []
for _ in range(4):
    tamaño_barras.append(randrange(1,8))
lista_ordenada = sorted(tamaño_barras)
while 1<tamaño_barras.count(0) or lista_ordenada[0]==lista_ordenada[1] or lista_ordenada[-2]==lista_ordenada[-1]:
    tamaño_barras = []
    for _ in range(4):
        tamaño_barras.append(randrange(1,8))
    lista_ordenada = sorted(tamaño_barras)

#juguetes vendidos
lista_de_juguetes_completa = ["Bicicleta", "Auto", "Moto", "Tren", "Lápiz", "Muñeco", "Lego", "Pirámide", "Cometa", "Robot", "Micrófono", "Plastilina", "Robot"]
shuffle(lista_de_juguetes_completa)
lista_de_juguetes = lista_de_juguetes_completa[0:len(tamaño_barras)]

#Ordena los juguetes
lista_de_clases = []
for i in range(len(tamaño_barras)):
    lista_de_clases.append(Juguete(lista_de_juguetes[i], tamaño_barras[i]))
lista_de_clases = sorted(lista_de_clases)






#================================Aquí va el enunciado================================================================
enunciado = r"""A continuación se muestra gráfico de barras de los juguetes vendidos en una tienda
"""+   tabla(lista_de_juguetes, range(1, max(tamaño_barras)+1), tamaño_barras)


if opcion==1:
    enunciado += "El juguete más vendido es "

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(lista_de_clases[3])
    contenido_2 =        Matematica(lista_de_clases[2])
    contenido_3 =        Matematica(lista_de_clases[1])
    contenido_4 =        Matematica(lista_de_clases[0])
    contenido_5 =        Matematica(lista_de_juguetes_completa[-1])



elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado += "El juguete menos vendido es "

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(lista_de_clases[0])
    contenido_2 =        Matematica(lista_de_clases[1])
    contenido_3 =        Matematica(lista_de_clases[2])
    contenido_4 =        Matematica(lista_de_clases[3])
    contenido_5 =        Matematica(lista_de_juguetes_completa[-1])



elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado += "La cantidad total de juguetes vendidos es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(tamaño_barras[0]+tamaño_barras[1]+tamaño_barras[2]+tamaño_barras[3])
    contenido_2 =        Matematica(tamaño_barras[0])
    contenido_3 =        Matematica(tamaño_barras[1])
    contenido_4 =        Matematica(tamaño_barras[2])
    contenido_5 =        Matematica(tamaño_barras[3])



enunciado_oculto = [opcion, sorted(tamaño_barras)]












