{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
ea, eb, ec, ed = Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15))
while ea+ed-eb-ec==0:
    ea, eb, ec, ed = Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15))
x = (ec*eb-ea*ed)/(ea+ed-eb-ec)
while ea+ed-eb-ec==0 or eb+ed-ea-ec==0 or ec*eb-ea*ed==0 or ec*ea-eb*ed==0 or x+ea<=0 or x+eb<=0 or x+ec<=0 or x+ed<=0 or ea<=ed or eb<=ec:
    ea, eb, ec, ed = Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15))
    while ea+ed-eb-ec==0:
        ea, eb, ec, ed = Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15))
    x = (ec*eb-ea*ed)/(ea+ed-eb-ec)



angulo_4 = randrange(10,50)
angulo_1 = 180-angulo_4-randrange(30, 40)
angulo_3 = randrange(-45, -10)
angulo_2 = -180-angulo_3+randrange(20, 30)
angulo_de_giro = Racional(randrange(0, 360))

lista_de_letras = ["A","B","C","D","E"]

letra_A = choice(lista_de_letras)
lista_de_letras.remove(letra_A)
letra_B = choice(lista_de_letras)
lista_de_letras.remove(letra_B)
letra_C = choice(lista_de_letras)
lista_de_letras.remove(letra_C)
letra_D = choice(lista_de_letras)
lista_de_letras.remove(letra_D)
letra_E = choice(lista_de_letras)
lista_de_letras.remove(letra_E)

letra_A, letra_B, letra_C, letra_D, letra_E = "A", "B", "C", "D", "E"

# A  D
#       E
# B  C
unidad_de_medida = choice(["mm", "cm", "m", "km"])

#================================Aquí va el enunciado================================================================
enunciado = fr"""En la siguiente figura los puntos {Matematica(letra_A)}, {Matematica(letra_B)}, {Matematica(letra_C)} y {Matematica(letra_D)} están sobre la circunferencia
\begin{{center}}
\begin{{tikzpicture}} [scale=1.5]

\draw (0,0) circle(1);

\tkzDefPoint({angulo_1+angulo_de_giro}:1){{{letra_A}}}
\tkzDefPoint({angulo_2+angulo_de_giro}:1){{{letra_B}}}
\tkzDefPoint({angulo_3+angulo_de_giro}:1){{{letra_C}}}
\tkzDefPoint({angulo_4+angulo_de_giro}:1){{{letra_D}}}
\tkzInterLL({letra_B},{letra_C})({letra_A},{letra_D}) \tkzGetPoint{{{letra_E}}}

\tkzDrawSegment({letra_A},{letra_E})
\tkzDrawSegment({letra_B},{letra_E})

\node [label={angulo_1+angulo_de_giro}:{letra_A}] at ({letra_A}){{}};
\node [label={angulo_2+angulo_de_giro}:{letra_B}] at ({letra_B}){{}};
\node [label={angulo_3-10+angulo_de_giro}:{letra_C}] at ({letra_C}){{}};
\node [label={angulo_4+10+angulo_de_giro}:{letra_D}] at ({letra_D}){{}};
\node [label={choice([90,270])+angulo_de_giro}:{letra_E}] at ({letra_E}){{}};

\end{{tikzpicture}} \end{{center}}
Si {Matematica(linea(letra_E+letra_D))} mide {Matematica(Pol("x",ed,parentesis=True)+" "+unidad_de_medida,arreglar_espacios=True)}, {Matematica(linea(letra_E+letra_A))} mide {Matematica(Pol("x",ea,parentesis=True)+" "+unidad_de_medida,arreglar_espacios=True)}, {Matematica(linea(letra_E+letra_C))} mide {Matematica(Pol("x",ec,parentesis=True)+" "+unidad_de_medida,arreglar_espacios=True)} y {Matematica(linea(letra_E+letra_B))} mide {Matematica(Pol("x",eb,parentesis=True)+" "+unidad_de_medida,arreglar_espacios=True)}, ¿cuál es el valor de x?"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica((ec*eb-ea*ed)/(ea+ed-eb-ec))
contenido_2 = Matematica((ec*ea-eb*ed)/(eb+ed-ea-ec))
contenido_3 = Matematica((ea+ed-eb-ec)/(ec*eb-ea*ed))
contenido_4 = Matematica((eb+ed-ea-ec)/(ec*ea-eb*ed))
contenido_5 = Matematica(ea+eb+ec+ed)



enunciado_oculto = [ea, eb, ec, ed]











