{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
primer_angulo, segundo_angulo, tercer_angulo, cuarto_angulo = randrange(0, 90), randrange(90,180), randrange(180,270), randrange(270,360)
while segundo_angulo-primer_angulo<40 or tercer_angulo-segundo_angulo<40 or cuarto_angulo-segundo_angulo<40 or (360-cuarto_angulo)+primer_angulo<40:
    primer_angulo, segundo_angulo, tercer_angulo, cuarto_angulo = randrange(0, 90), randrange(90,180), randrange(180,270), randrange(270,360)
    
ea, eb, ec = Racional(randrange(1, 15)), Racional(randrange(1, 15)), Racional(randrange(1, 15))

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

# letra_A, letra_B, letra_C, letra_D, letra_E = "A", "B", "C", "D", "E"

unidad_de_medida = choice(["mm", "cm", "m", "km"])


#================================Aquí va el enunciado================================================================
enunciado = fr"""En la siguiente figura los puntos {Matematica(letra_A)}, {Matematica(letra_B)}, {Matematica(letra_C)} y {Matematica(letra_D)} están sobre la circunferencia y {Matematica(letra_E)} es el punto de intersección entre los segmentos {Matematica(linea(letra_A+letra_C))} y {Matematica(linea(letra_B+letra_D))}
\begin{{center}}
\begin{{tikzpicture}} [scale=1.5]

\draw (0,0) circle(1);

\tkzDefPoint({primer_angulo+angulo_de_giro}:1){{{letra_A}}}
\tkzDefPoint({segundo_angulo+angulo_de_giro}:1){{{letra_B}}}
\tkzDefPoint({tercer_angulo+angulo_de_giro}:1){{{letra_C}}}
\tkzDefPoint({cuarto_angulo+angulo_de_giro}:1){{{letra_D}}}
\tkzInterLL({letra_A},{letra_C})({letra_B},{letra_D}) \tkzGetPoint{{{letra_E}}}

\tkzDrawPoints({letra_A},{letra_B},{letra_C},{letra_D},{letra_E})

\tkzDrawSegment({letra_A},{letra_C})
\tkzDrawSegment({letra_B},{letra_D})

\node [label={primer_angulo+angulo_de_giro}:{letra_A}] at ({letra_A}){{}};
\node [label={segundo_angulo+angulo_de_giro}:{letra_B}] at ({letra_B}){{}};
\node [label={tercer_angulo+angulo_de_giro}:{letra_C}] at ({letra_C}){{}};
\node [label={cuarto_angulo+angulo_de_giro}:{letra_D}] at ({letra_D}){{}};
\node [label={int(segundo_angulo/2)+primer_angulo+angulo_de_giro}:{letra_E}] at ({letra_E}){{}};

\end{{tikzpicture}} \end{{center}}
Si {Matematica(linea(letra_E+letra_A))} mide {Matematica(ea)} {unidad_de_medida}, {Matematica(linea(letra_E+letra_B))} mide {Matematica(eb)} {unidad_de_medida} y {Matematica(linea(letra_E+letra_C))} mide {Matematica(ec)} {unidad_de_medida}, """

if opcion == 1:
    enunciado += f"¿cuánto mide {Matematica(linea(letra_E+letra_D))}?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(ea*ec/eb)+" "+unidad_de_medida
    contenido_2 = Matematica(eb*ec/ea)+" "+unidad_de_medida
    contenido_3 = Matematica(ea*eb/ec)+" "+unidad_de_medida
    contenido_4 = Matematica(eb/(ea*ec))+" "+unidad_de_medida
    contenido_5 = Matematica(ea*ec/eb+eb)+" "+unidad_de_medida

elif opcion == 2:
    enunciado += f"¿cuánto mide {Matematica(linea(letra_B+letra_D))}?"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(ea*ec/eb+eb)+" "+unidad_de_medida
    contenido_2 = Matematica(eb*ec/ea)+" "+unidad_de_medida
    contenido_3 = Matematica(ea*eb/ec)+" "+unidad_de_medida
    contenido_4 = Matematica(eb/(ea*ec))+" "+unidad_de_medida
    contenido_5 = Matematica(ea*ec/eb)+" "+unidad_de_medida



enunciado_oculto = [opcion, ea, eb, ec]











