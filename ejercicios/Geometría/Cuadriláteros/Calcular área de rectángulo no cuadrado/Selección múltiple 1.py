{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
b, h = Racional(randrange(1, 11)), Racional(randrange(1, 11))
while b==h:
    b, h = Racional(randrange(1, 11)), Racional(randrange(1, 11))

unidad_de_medida = choice(["mm", "cm", "m", "km"])
base_dibujo = randrange(2,11)
altura_dibujo = randrange(2,6)
while base_dibujo == altura_dibujo:
    base_dibujo = randrange(2,11)
    altura_dibujo = randrange(2,6)

#================================Aquí va el enunciado================================================================
enunciado = fr"""Sea el rectángulo ABCD que se muestra a continuación
\begin{{center}}
\begin{{tikzpicture}} [scale=0.5]
\tkzDefPoint(0,0){{A}}
\tkzDefPoint({base_dibujo},0){{B}}
\tkzDefPoint({base_dibujo},{altura_dibujo}){{C}}
\tkzDefPoint(0,{altura_dibujo}){{D}}
\tkzDrawPolygon(A,B,C,D)
\node [label=225:A] at (A) {{}};
\node [label=315:B] at (B) {{}};
\node [label=45:C] at (C) {{}};
\node [label=135:D] at (D) {{}};
\tkzLabelSegment{choice([f"[below](A,B){{{b} {unidad_de_medida}}}", f"[above](C,D){{{b} {unidad_de_medida}}}"])}
\tkzLabelSegment{choice([f"[right](B,C){{{h} {unidad_de_medida}}}", f"[left](D,A){{{h} {unidad_de_medida}}}"])}
\end{{tikzpicture}}
\end{{center}}
El área de ABCD es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(b*h+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_2 = Matematica((2*b+2*h)+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_3 = Matematica(b*h/2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_4 = Matematica((b+h)+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_5 = Matematica((b+h)/2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))



enunciado_oculto = [b, h]











