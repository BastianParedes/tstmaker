{"cantidad_opciones":3, "cantidad_disponible":50}

unidad_de_medida = choice(["mm", "cm", "m", "km"])

if opcion==1:#Rectángulo
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    while True:
        p_1 = Pol(elegir(-9,10,0), Term(elegir(-9,10,0),{"x":1}), azar=True, parentesis=True)
        p_2 = Pol(elegir(-9,10,0), Term(elegir(-9,10,0),{"x":1}), azar=True, parentesis=True)
        if p_1 != p_2 and p_1 != -p_2:
            break

    while True:
        ancho_dibujo = uniform(1,3)
        alto_dibujo = uniform(1,3)
        if abs(ancho_dibujo-alto_dibujo) < 0.5:
            break

    #================================Aquí va el enunciado================================================================
    partes_enunciado = [
        "el lado " + choice(["AB","BA","CD","DC"]) + " mide "+Matematica(p_1)+" "+unidad_de_medida,
        "el lado " + choice(["AD","DA","CB","BC"]) + " mide "+Matematica(p_2)+" "+unidad_de_medida,
    ]
    shuffle(partes_enunciado)
    parte_1_del_enunciado = partes_enunciado[0]
    parte_0_del_enunciado = partes_enunciado[1]
    enunciado = fr"""En el siguiente rectángulo se cumple que {parte_1_del_enunciado} y {parte_0_del_enunciado}
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate=0]
\coordinate (A) at (0,0);
\coordinate (B) at ({ancho_dibujo},0);
\coordinate (C) at ({ancho_dibujo},{alto_dibujo});
\coordinate (D) at (0,{alto_dibujo});

\tkzDrawPolygon(A,B,C,D);

\node at ($(A)+(225:0.2)$) {{A}};
\node at ($(B)+(-45:0.2)$) {{B}};
\node at ($(C)+(45:0.2)$) {{C}};
\node at ($(D)+(135:0.2)$) {{D}};

\tkzDrawPoints[fill=black](A,B,C,D)
\end{{tikzpicture}} \end{{center}}
El área del rectángulo está dado por la expresión"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+(p_1*p_2)+") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #solo multiplica los que están en medio
    contenido_2 =        Matematica("("+Pol(lista_de_terminos=  p_1.lista_de_terminos[:-1] + [p_1.lista_de_terminos[-1]*p_2.lista_de_terminos[0]] + p_2.lista_de_terminos[1:]  , reducir=True)      +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma los polinomios
    contenido_3 =        Matematica("("+(p_1 + p_2)   +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma muchas veces en lugar de multiplicar muchas veces.
    lista_provisional_1 = []
    for t_1 in p_1.lista_de_terminos:
        for t_2 in p_2.lista_de_terminos:
            lista_provisional_1.append(Pol(t_1,t_2,reducir=True))
    lista_provisional_2 = []
    for polinomio in lista_provisional_1:
        for termino in polinomio.lista_de_terminos:
            lista_provisional_2.append(termino)
    contenido_4 =        Matematica("("+(Pol(lista_de_terminos=lista_provisional_2,reducir=True))     +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma las partes numericas a las t_2
    lista_provisional = []
    for t_1 in p_1.lista_de_terminos:
        for t_2 in p_2.lista_de_terminos:
            lista_provisional.append(Term(t_1.factor_numerico+t_2.factor_numerico , t_2.diccionario_de_letras_y_exponentes))
    contenido_5 =        Matematica("("+(Pol(lista_de_terminos=lista_provisional,reducir=True))   +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))






if opcion==2:#Cuadrado
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    p_1 = Pol(elegir(-9,10,0), Term(elegir(-9,10,0),{"x":1}), azar=True, parentesis=True)
    p_2 = p_1

    lado_dibujo = uniform(1,3)

    #================================Aquí va el enunciado================================================================
    lado = choice(["AB","BA","CD","DC","AD","DA","CB","BC"])
    enunciado = fr"""La figura ABCD es cuadrado cuyos lados miden {Matematica(p_1)} {unidad_de_medida}
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate=0]
\coordinate (A) at (0,0);
\coordinate (B) at ({lado_dibujo},0);
\coordinate (C) at ({lado_dibujo},{lado_dibujo});
\coordinate (D) at (0,{lado_dibujo});

\tkzDrawPolygon(A,B,C,D);

\node at ($(A)+(225:0.2)$) {{A}};
\node at ($(B)+(-45:0.2)$) {{B}};
\node at ($(C)+(45:0.2)$) {{C}};
\node at ($(D)+(135:0.2)$) {{D}};

\tkzDrawPoints[fill=black](A,B,C,D)
\end{{tikzpicture}} \end{{center}}
El área del cuadrado está dado por la expresión"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+(p_1*p_2)+") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #solo multiplica los que están en medio
    contenido_2 =        Matematica("("+Pol(lista_de_terminos=  p_1.lista_de_terminos[:-1] + [p_1.lista_de_terminos[-1]*p_2.lista_de_terminos[0]] + p_2.lista_de_terminos[1:]  , reducir=True)      +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma los polinomios
    contenido_3 =        Matematica("("+(p_1 + p_2)   +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma muchas veces en lugar de multiplicar muchas veces.
    lista_provisional_1 = []
    for t_1 in p_1.lista_de_terminos:
        for t_2 in p_2.lista_de_terminos:
            lista_provisional_1.append(Pol(t_1,t_2,reducir=True))
    lista_provisional_2 = []
    for polinomio in lista_provisional_1:
        for termino in polinomio.lista_de_terminos:
            lista_provisional_2.append(termino)
    contenido_4 =        Matematica("("+(Pol(lista_de_terminos=lista_provisional_2,reducir=True))     +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma las partes numericas a las t_2
    lista_provisional = []
    for t_1 in p_1.lista_de_terminos:
        for t_2 in p_2.lista_de_terminos:
            lista_provisional.append(Term(t_1.factor_numerico+t_2.factor_numerico , t_2.diccionario_de_letras_y_exponentes))
    contenido_5 =        Matematica("("+(Pol(lista_de_terminos=lista_provisional,reducir=True))   +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))








elif opcion==3:#Triángulo
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    p_1 = Pol(elegir(-5,5,0)*2, Term(elegir(-5,5,0)*2,{"x":1}), azar=True, parentesis=True)
    p_2 = Pol(elegir(-9,10,0), Term(elegir(-9,10,0),{"x":1}), azar=True, parentesis=True)
    lista_provisional = [p_1,p_2]
    shuffle(lista_provisional)
    p_1, p_2 = lista_provisional[0], lista_provisional[1]


    #================================Aquí va el enunciado================================================================
    partes_enunciado = [
        "el lado " + choice(["AB","BA"]) + " mide "+Matematica(p_1)+" "+unidad_de_medida,
        "el lado " + choice(["CD","DC"]) + " mide "+Matematica(p_2)+" "+unidad_de_medida,
    ]
    shuffle(partes_enunciado)
    parte_1_del_enunciado = partes_enunciado[0]
    parte_0_del_enunciado = partes_enunciado[1]
    enunciado = fr"""En el siguiente triángulo ABC se cumple que {parte_1_del_enunciado} y {parte_0_del_enunciado}
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate=0]
\coordinate (A) at ({-uniform(1,3)},0);
\coordinate (B) at ({uniform(1,3)},0);
\coordinate (C) at (0,{uniform(1,3)});
\coordinate (D) at (0,0);

\draw (C) -- (A) -- (B) -- (C) -- (D);

\tkzMarkRightAngle[size=0.3]({choice(["B,D,C","C,D,A"])})

\node at ($(A)+(225:0.2)$) {{A}};
\node at ($(B)+(-45:0.2)$) {{B}};
\node at ($(C)+(90:0.2)$) {{C}};
\node at ($(D)+(-90:0.2)$) {{D}};

\tkzDrawPoints[fill=black](A,B,C,D)
\end{{tikzpicture}} \end{{center}}
El área del triángulo ABC está dado por la expresión"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica("("+(p_1*p_2)+") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #solo multiplica los que están en medio
    contenido_2 =        Matematica("("+Pol(lista_de_terminos=  p_1.lista_de_terminos[:-1] + [p_1.lista_de_terminos[-1]*p_2.lista_de_terminos[0]] + p_2.lista_de_terminos[1:]  , reducir=True)      +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma los polinomios
    contenido_3 =        Matematica("("+(p_1 + p_2)   +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma muchas veces en lugar de multiplicar muchas veces.
    lista_provisional_1 = []
    for t_1 in p_1.lista_de_terminos:
        for t_2 in p_2.lista_de_terminos:
            lista_provisional_1.append(Pol(t_1,t_2,reducir=True))
    lista_provisional_2 = []
    for polinomio in lista_provisional_1:
        for termino in polinomio.lista_de_terminos:
            lista_provisional_2.append(termino)
    contenido_4 =        Matematica("("+(Pol(lista_de_terminos=lista_provisional_2,reducir=True))     +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))

    #suma las partes numericas a las t_2
    lista_provisional = []
    for t_1 in p_1.lista_de_terminos:
        for t_2 in p_2.lista_de_terminos:
            lista_provisional.append(Term(t_1.factor_numerico+t_2.factor_numerico , t_2.diccionario_de_letras_y_exponentes))
    contenido_5 =        Matematica("("+(Pol(lista_de_terminos=lista_provisional,reducir=True))   +") "+potencia(unidad_de_medida,2, parentesis_automatico=False))




enunciado_oculto = [p_1,p_2]












