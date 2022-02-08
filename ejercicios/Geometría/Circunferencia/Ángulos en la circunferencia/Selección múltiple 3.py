{"cantidad_opciones":2, "cantidad_disponible":2}

if opcion==1:#2019 ejercicio 47
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la circunferencia de centro O de la figura adjunta los puntos R, S y T pertenecen a ella. Se puede determinar la medida del $\sphericalangle \mathrm{{OTR}}$, si se sabe que:
\begin{{center}} \begin{{tikzpicture}} [scale=1.5, rotate={randrange(0,360)}]
\tkzDefPoint(0,0){{O}}
\tkzDefPoint(240:1){{R}}
\tkzDefPoint(-20:1){{S}}
\tkzDefPoint(90:1){{T}}

\tkzDrawPolygon(T,R,S);
\draw (T) -- (O) -- (R);

\node at ($(O)+(-20:0.15)$) {{O}};
\node at ($(R)+(258:0.15)$) {{R}};
\node at ($(S)+(-20:0.15)$) {{S}};
\node at ($(T)+(90:0.15)$) {{T}};

\draw (0,0) circle(1);
\end{{tikzpicture}} \end{{center}}"""
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"$\sphericalangle \mathrm{{OTS}}=35\degree$"
    informacion_2 = r"$\sphericalangle \mathrm{{TSR}}=84\degree$"
    alternativa_correcta = "B"



elif opcion==2:#2017 ejercicio 75
    #================================Aquí va el enunciado================================================================
    enunciado = r"""En la circunferencia de centro O de la figura adjunta los puntos M, Q y P pertenecen a ella. Se puede determinar la medida del ángulo x, si:
\begin{center} \begin{tikzpicture} [scale=1.5, rotate="""+str(randrange(0,360))+r"""]
\tkzDefPoint(0,0){O}
\tkzDefPoint(210:1){M}
\tkzDefPoint(90:1){P}
\tkzDefPoint(330:1){Q}

\node at ($(O)+(90:0.15)$){O};
\node at ($(M)+(210:0.15)$){M};
\node at ($(P)+(90:0.15)$){P};
\node at ($(Q)+(330:0.15)$){Q};

\draw (M) -- (O) -- (Q) -- (P) -- (M);
\draw (0,0) circle(1);
\draw pic["x",draw,angle radius=1cm] {angle=O--M--P};
\end{tikzpicture} \end{center}"""
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = "Se conoce la medida del ángulo MOQ."
    informacion_2 = r"$\mathrm{\overline{MP} \cong \overline{PQ}}$"
    alternativa_correcta = "C"










