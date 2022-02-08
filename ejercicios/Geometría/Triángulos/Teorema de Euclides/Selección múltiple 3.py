{"cantidad_opciones":1, "cantidad_disponible":1}

if opcion==1:# PSU 2015 ejercicio 78
    #================================Aquí va el enunciado================================================================
    enunciado = r"""En el triángulo ACD de la figura adjunta, se puede determinar la medida del segmento BC, si:
\begin{center} \begin{tikzpicture} [scale=2, rotate="""+str(randrange(0,360))+r"""]
\coordinate (A) at (-1,0);
\coordinate (C) at (1,0);
"""+fr"""\coordinate (D) at ({randrange(60,140)}:1);"""+r"""
\coordinate (B) at ($(A)!(D)!(C)$);

\node at ($(A)+(-90:0.15)$){A};
\node at ($(B)+(-90:0.15)$){B};
\node at ($(C)+(-90:0.15)$){C};
\node at ($(D)+(90:0.15)$){D};

\draw (D) -- (A) -- (C) -- (D) -- (B);

\tkzMarkRightAngle[size=0.11](C,B,D);
\tkzMarkRightAngle[size=0.11](A,D,C);
\end{tikzpicture} \end{center}"""
    #================================Aquí están los contenidos de las informaciones. También la alternativa correcta=====
    informacion_1 = r"$\mathrm{AB=3\ cm}$"
    informacion_2 = "Se conoce la medida del segmento DC."
    alternativa_correcta = "C"












