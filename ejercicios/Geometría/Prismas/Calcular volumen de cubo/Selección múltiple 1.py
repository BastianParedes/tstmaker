{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
arista = Racional(randrange(1,55))
unidad_de_medida = choice(["mm", "cm", "m", "km"])

#================================Aquí va el enunciado================================================================
enunciado = fr"""Considera un cubo cuyas aristas miden {Matematica(arista+" "+unidad_de_medida, arreglar_espacios=True)}. El volumen de dicho cubo es
\begin{{center}} \begin{{tikzpicture}} [scale={randrange(10,20)/10}, rotate={randrange(0,360)}]
\coordinate (A1) at (0,0);
\coordinate (A2) at (1,0);
\coordinate (A3) at ($(A2)+(45:0.8)$);
\coordinate (A') at ($(A1)!0.5!(A3)$);
\coordinate (A4) at ($(A2)!2!(A')$);

\coordinate (B1) at ($(A1)+(0,1)$);
\coordinate (B2) at ($(A2)+(0,1)$);
\coordinate (B3) at ($(A3)+(0,1)$);
\coordinate (B4) at ($(A4)+(0,1)$);

\draw [dashed] (A3) -- (A4) -- (A1);
\draw [dashed] (A4) -- (B4);
\draw (A2) -- (B2) -- (B1) -- (A1) -- (A2) -- (A3) -- (B3) -- (B4) -- (B1);
\draw (B2) -- (B3);
\end{{tikzpicture}} \end{{center}}"""

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(arista**3 + " " + potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_2 =        Matematica(6*arista**2 + " " + potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_3 =        Matematica(arista**2 + " " + potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_4 =        Matematica(6*arista**3 + " " + potencia(unidad_de_medida,3,parentesis_automatico=False))
contenido_5 =        Matematica(3*arista + " " + potencia(unidad_de_medida,3,parentesis_automatico=False))



enunciado_oculto = arista











