{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
lado = Racional(randrange(1, 55))
unidad_de_medida = choice(["mm", "cm", "m", "km"])
lado_dibujo = randrange(2,6)

#================================Aquí va el enunciado================================================================
enunciado = fr"""Sea el cuadrado ABCD que se muestra a continuación
\begin{{center}}
\begin{{tikzpicture}} [scale=0.5]
\tkzDefPoint(0,0){{A}}
\tkzDefPoint({lado_dibujo},0){{B}}
\tkzDefPoint({lado_dibujo},{lado_dibujo}){{C}}
\tkzDefPoint(0,{lado_dibujo}){{D}}
\tkzDrawPolygon(A,B,C,D)
\node [label=225:A] at (A) {{}};
\node [label=315:B] at (B) {{}};
\node [label=45:C] at (C) {{}};
\node [label=135:D] at (D) {{}};
\tkzLabelSegment{choice([f"[below](A,B){{{lado} {unidad_de_medida}}}", f"[above](C,D){{{lado} {unidad_de_medida}}}", f"[right](B,C){{{lado} {unidad_de_medida}}}", f"[left](D,A){{{lado} {unidad_de_medida}}}"])}
\end{{tikzpicture}}
\end{{center}}
El perímetro de ABCD es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(4*lado+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_2 = Matematica(lado**2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_3 = Matematica(lado+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_4 = Matematica(lado*2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))
contenido_5 = Matematica(lado/2+" "+potencia(unidad_de_medida,2,parentesis_automatico=False))



enunciado_oculto = lado











