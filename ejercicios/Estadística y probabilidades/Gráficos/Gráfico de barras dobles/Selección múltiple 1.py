{"cantidad_opciones":5, "cantidad_disponible":50}

def tabla(eje_x, eje_y, valores_1, valores_2, titulo=""):
    divisor = eje_y[0]
    separacion_horizontal = 1.4
    separacion_vertical = 0.5
    resultado = r"\begin{center} "+fr"""\begin{{tikzpicture}}[scale=1]
\draw [->] (0,0) -- ({len(eje_x)*separacion_horizontal+separacion_horizontal/2-0.2}, 0);
\draw [->] (0,-0.2) -- (0, {len(eje_y)*separacion_vertical+separacion_vertical/2+0.1});
\node [font=\scriptsize, rotate=90] at ({len(eje_x)*separacion_horizontal+separacion_horizontal/2}, 0) {{Año}};
\node [font=\scriptsize] at (-0.2, 0) {{0}};
\node [font=\scriptsize] at (0, {len(eje_y)*separacion_vertical+separacion_vertical/2+0.3}) {{Cantidad}};"""
    x = len(eje_x)*separacion_horizontal+separacion_horizontal/2
    y = 1.5
    medio_lado = 0.1
    resultado += fr"""
\filldraw[draw=black,fill=gray!200] plot coordinates{{ ({x-medio_lado},{y-medio_lado}) ({x+medio_lado},{y-medio_lado}) ({x+medio_lado},{y+medio_lado}) ({x-medio_lado},{y+medio_lado}) ({x-medio_lado},{y-medio_lado}) }};
\node [label={{[font=\scriptsize]right:Hombres}}] at ({x+0.05}, {y}) {{}};"""
    y = 1
    resultado += fr"""
\filldraw[draw=black,fill=gray!50] plot coordinates{{ ({x-medio_lado},{y-medio_lado}) ({x+medio_lado},{y-medio_lado}) ({x+medio_lado},{y+medio_lado}) ({x-medio_lado},{y+medio_lado}) ({x-medio_lado},{y-medio_lado}) }};
\node [label={{[font=\scriptsize]right:Mujeres}}] at ({x+0.05}, {y}) {{}};

"""

    medio_ancho = 0.15
    media_separacion = 0.25
    #Lineas horizontañes
    for i in range(len(eje_y)):
        resultado += fr"\draw [dashed] (0, {separacion_vertical*(i+1)}) -- ({separacion_horizontal*len(eje_x)}, {separacion_vertical*(i+1)});" + "\n"

    #Etiquetas eje y
    for i in range(len(eje_y)):
        resultado += fr"\node [font=\scriptsize] at (-0.2, {separacion_vertical*(i+1)}) {{{eje_y[i]}}};"+"\n"

    #Primeras barras
    for i in range(len(valores_1)):
        x, y = separacion_horizontal*(i+1)-2*media_separacion, valores_1[i]*separacion_vertical/divisor
        resultado += fr"\filldraw[draw=black,fill=gray!200] plot coordinates{{ ({x-2*medio_ancho},0) ({x},0) ({x},{y}) ({x-2*medio_ancho},{y}) ({x-2*medio_ancho},0) }};"+"\n"

    #Segundas barras
    for i in range(len(valores_2)):
        x, y = separacion_horizontal*(i+1), valores_2[i]*separacion_vertical/divisor
        resultado += fr"\filldraw[draw=black,fill=gray!50] plot coordinates{{ ({x-2*medio_ancho},0) ({x},0) ({x},{y}) ({x-2*medio_ancho},{y}) ({x-2*medio_ancho},0) }};"+"\n"

    #Etiquetas exe x
    for i in range(len(valores_1)):
        x = separacion_horizontal*(i+1)-medio_ancho-media_separacion
        y = -0.2
        resultado += fr"\node [font=\scriptsize] at ({x}, {y}) {{{eje_x[i]}}};"+"\n"

    return resultado + r"\end{tikzpicture} \end{center}"




def suma_de_elementos(lista):
    resultado = 0
    for i in lista:
        resultado += int(i)
    return resultado


#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
#juguetes vendidos
dominio = [randrange(2000, 2017)]
for i in range(1,3):
    dominio.append(dominio[0]+i)

# Tamaño de las primeras barras
tamaño_primeras_barras = []
for _ in range(len(dominio)):
    tamaño_primeras_barras.append(randrange(1,11))

# Tamaño de las segundas barras
tamaño_segundas_barras = []
for _ in range(len(dominio)):
    tamaño_segundas_barras.append(randrange(1,11))

#================================Aquí va el enunciado================================================================
enunciado = r"""A continuación se muestra un gráfico de doble barra que muestra la cantidad de autos comprados en cierta tienda por hombres y mujeres
"""+   tabla(dominio, [2,4,6,8,10], tamaño_primeras_barras, tamaño_segundas_barras)




if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado += "La cantidad total de autos vendidos es "
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    #Suma de todos los autos
    contenido_correcto = Matematica(suma_de_elementos(tamaño_primeras_barras) + suma_de_elementos(tamaño_segundas_barras))
    #Suma de los autos comprados por los hombres
    contenido_2 =        Matematica(suma_de_elementos(tamaño_primeras_barras))
    #Suma de los autos comprados por las mujeres
    contenido_3 =        Matematica(suma_de_elementos(tamaño_segundas_barras))
    #Suma de los autos comprados el primer año
    contenido_4 =        Matematica(tamaño_primeras_barras[0] + tamaño_segundas_barras[0])
    #Suma de los autos comprados el último año
    contenido_5 =        Matematica(tamaño_primeras_barras[-1] + tamaño_segundas_barras[-1])





elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado += "La cantidad de autos comprados por los hombres es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(suma_de_elementos(tamaño_primeras_barras))
    contenido_2 =        Matematica(suma_de_elementos(tamaño_primeras_barras) + suma_de_elementos(tamaño_segundas_barras))
    contenido_3 =        Matematica(suma_de_elementos(tamaño_segundas_barras))
    contenido_4 =        Matematica(tamaño_primeras_barras[0] + tamaño_segundas_barras[0])
    contenido_5 =        Matematica(tamaño_primeras_barras[-1] + tamaño_segundas_barras[-1])






elif opcion==3:
    #================================Aquí va el enunciado================================================================
    enunciado += "La cantidad de autos comprados por mujeres es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(suma_de_elementos(tamaño_segundas_barras))
    contenido_2 =        Matematica(suma_de_elementos(tamaño_primeras_barras))
    contenido_3 =        Matematica(suma_de_elementos(tamaño_primeras_barras) + suma_de_elementos(tamaño_segundas_barras))
    contenido_4 =        Matematica(tamaño_primeras_barras[0] + tamaño_segundas_barras[0])
    contenido_5 =        Matematica(tamaño_primeras_barras[-1] + tamaño_segundas_barras[-1])






elif opcion==4:
    #================================Aquí va el enunciado================================================================
    enunciado += f"La cantidad de autos comprados el año {dominio[0]}"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(tamaño_primeras_barras[0] + tamaño_segundas_barras[0])
    contenido_2 =        Matematica(suma_de_elementos(tamaño_primeras_barras))
    contenido_3 =        Matematica(suma_de_elementos(tamaño_segundas_barras))
    contenido_4 =        Matematica(suma_de_elementos(tamaño_primeras_barras) + suma_de_elementos(tamaño_segundas_barras))
    contenido_5 =        Matematica(tamaño_primeras_barras[-1] + tamaño_segundas_barras[-1])






elif opcion==5:
    #================================Aquí va el enunciado================================================================
    enunciado += f"La cantidad de autos comprados el año {dominio[-1]}"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(tamaño_primeras_barras[-1] + tamaño_segundas_barras[-1])
    contenido_2 =        Matematica(suma_de_elementos(tamaño_primeras_barras))
    contenido_3 =        Matematica(suma_de_elementos(tamaño_segundas_barras))
    contenido_4 =        Matematica(tamaño_primeras_barras[0] + tamaño_segundas_barras[0])
    contenido_5 =        Matematica(suma_de_elementos(tamaño_primeras_barras) + suma_de_elementos(tamaño_segundas_barras))




enunciado_oculto = [tamaño_primeras_barras, tamaño_segundas_barras]











