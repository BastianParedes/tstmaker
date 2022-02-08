{"cantidad_opciones":1, "cantidad_disponible":1}

if opcion==1:#PSU 2020 ejercicio 47 modificado. Consideré que el dibujo no era necesario.
    angulo_1 = randrange(90,270)
    #================================Aquí va el enunciado================================================================
    enunciado = r"""Sean los triángulos ABC y DEF:
\begin{center} \begin{tikzpicture} [scale=0.35, rotate="""+f"{randrange(0,360)}"+r"""]
\coordinate (A) at (-4,1);
\coordinate (B) at (-1,2);
\coordinate (C) at (-5,6);
\coordinate (O) at (0,0);
"""+fr"""
\tkzDefPointBy[rotation=center O angle {angulo_1}](A) \tkzGetPoint{{D}}
\tkzDefPointBy[rotation=center O angle {angulo_1}](B) \tkzGetPoint{{E}}
\tkzDefPointBy[rotation=center O angle {angulo_1}](C) \tkzGetPoint{{F}}
"""+r"""
\node at ($(A)+(225:0.4)$) {A};
\node at ($(B)+(0:0.4)$) {B};
\node at ($(C)+(135:0.4)$) {C};
"""+fr"""
\node at ($(D)+({225+angulo_1}:0.4)$) {{D}};
\node at ($(E)+({0+angulo_1}:0.4)$) {{E}};
\node at ($(F)+({135+angulo_1}:0.4)$) {{F}};
"""+r"""
\draw (A) --  (B) --  (C) --  (A);
\draw (D) --  (E) --  (F) --  (D);

\end{tikzpicture} \end{center}
Se puede determinar que estos triángulos son congruentes, si se sabe que:"""

    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = "los triángulos son semejantes de razón 1."
    informacion_2 = "el triángulo DEF se obtiene de una o más transformaciones isométricas del triángulo ABC."
    alternativa_correcta = "D"













