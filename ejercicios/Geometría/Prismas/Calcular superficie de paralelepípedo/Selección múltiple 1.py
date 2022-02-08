{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
x, y, z = Racional(randrange(1,10)), Racional(randrange(1,10)), Racional(randrange(1,10))

alto_dibujo = randrange(5,15)/10
unidad_de_medida = choice(["mm", "cm", "m", "km"])
angulo_de_giro = randrange(0,360)

#================================Aquí va el enunciado================================================================
enunciado = fr"""Observa el siguiente parelelepípedo
\begin{{center}} \begin{{tikzpicture}} [scale={randrange(10,15)/10}, rotate={angulo_de_giro}]
\coordinate (A1) at (0,0);
\coordinate (A2) at ({elegir(5,15)/10},0);
\coordinate (A3) at ($(A2)+({randrange(30,60)}:{elegir(7,20)/10})$);
\coordinate (A') at ($(A1)!0.5!(A3)$);
\coordinate (A4) at ($(A2)!2!(A')$);

\coordinate (B1) at ($(A1)+(0,{alto_dibujo})$);
\coordinate (B2) at ($(A2)+(0,{alto_dibujo})$);
\coordinate (B3) at ($(A3)+(0,{alto_dibujo})$);
\coordinate (B4) at ($(A4)+(0,{alto_dibujo})$);

\draw [dashed] (A3) -- (A4) -- (A1);
\draw [dashed] (A4) -- (B4);
\draw (A2) -- (B2) -- (B1) -- (A1) -- (A2) -- (A3) -- (B3) -- (B4) -- (B1);
\draw (B2) -- (B3);
"""+choice([fr"\coordinate [label={270+angulo_de_giro}:{x+' '+unidad_de_medida}] (x) at ($(A1)!0.5!(A2)$);",
            fr"\coordinate [label={90+angulo_de_giro}:{x+' '+unidad_de_medida}] (x) at ($(B3)!0.5!(B4)$);"
]) + choice([fr"\coordinate [label={-45+angulo_de_giro}:{y+' '+unidad_de_medida}] (y) at ($(A2)!0.5!(A3)$);",
             fr"\coordinate [label={135+angulo_de_giro}:{y+' '+unidad_de_medida}] (y) at ($(B1)!0.5!(B4)$);"
]) + choice([fr"\coordinate [label={0+angulo_de_giro}:{z+' '+unidad_de_medida}] (z) at ($(A3)!0.5!(B3)$);",
             fr"\coordinate [label={180+angulo_de_giro}:{z+' '+unidad_de_medida}] (z) at ($(A1)!0.5!(B1)$);"
]) + r"""\end{tikzpicture} \end{center}
La superficie de la figura es"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(2*(x*y+y*z+x*z)+" "+potencia(unidad_de_medida,2,parentesis_automatico=False),arreglar_espacios=True)
contenido_2 =        Matematica(x+y+z+" "+potencia(unidad_de_medida,2,parentesis_automatico=False),arreglar_espacios=True)
contenido_3 =        Matematica(x*y*z+" "+potencia(unidad_de_medida,2,parentesis_automatico=False),arreglar_espacios=True)
contenido_4 =        Matematica(2*(x+y+y+z+x+z)+" "+potencia(unidad_de_medida,2,parentesis_automatico=False),arreglar_espacios=True)
contenido_5 =        Matematica(x*y+y*z+x*z+" "+potencia(unidad_de_medida,2,parentesis_automatico=False),arreglar_espacios=True)




enunciado_oculto = sorted([x,y,z])











