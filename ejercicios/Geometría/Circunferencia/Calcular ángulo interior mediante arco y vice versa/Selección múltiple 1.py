{"cantidad_opciones":2, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    arco_derecho = Racional(randrange(40, 180, 2))
    arco_izquierdo = Racional(randrange(40, 180, 2))
    angulo_interior = (arco_derecho+arco_izquierdo)/2
    while not 35<angulo_interior<140:
        arco_derecho = Racional(randrange(40, 180, 2))
        arco_izquierdo = Racional(randrange(40, 180, 2))
        angulo_interior = (arco_derecho+arco_izquierdo)/2

    angulo_de_giro = Racional(randrange(0, 360))

    radio = "1.5"

    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura los arcos {Matematica("AB")} y {Matematica("CD")} miden {Matematica(potencia(arco_derecho,"°"))} y {Matematica(potencia(arco_izquierdo,"°"))} respectivamente.
\begin{{center}}
\begin{{tikzpicture}} [scale=1]

\draw (0,0) circle({radio});

\tkzDefPoint(0,0){{O}}
\tkzDefPoint({-arco_derecho/2+angulo_de_giro}:{radio}){{A}}
\tkzDefPoint({arco_derecho/2+angulo_de_giro}:{radio}){{B}}
\tkzDefPoint({180-arco_izquierdo/2+angulo_de_giro}:{radio}){{C}}
\tkzDefPoint({180+arco_izquierdo/2+angulo_de_giro}:{radio}){{D}}
\tkzInterLL(A,C)(B,D) \tkzGetPoint{{P}}

\tkzDrawPoints(A,B,C,D)

\node [label={-arco_derecho/2+angulo_de_giro}:A] at (A){{}};
\node [label={arco_derecho/2+angulo_de_giro}:B] at (B){{}};
\node [label={180-arco_izquierdo/2+angulo_de_giro}:C] at (C){{}};
\node [label={180+arco_izquierdo/2+angulo_de_giro}:D] at (D){{}};

\tkzDrawSegment(A,C)
\tkzDrawSegment(B,D)

\draw pic["$\alpha$",draw,angle radius=0.5cm] {{{choice(["angle=A--P--B", "angle=C--P--D"])}}};

\end{{tikzpicture}} \end{{center}}
¿Cuál es el valor de $\alpha$?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(angulo_interior+"°")
    contenido_2 = Matematica(arco_izquierdo+arco_derecho+"°")
    contenido_3 = Matematica(Racional(abs(arco_izquierdo-arco_derecho),2,True)+"°")
    contenido_4 = Matematica(abs(arco_izquierdo-arco_derecho)+"°")
    contenido_5 = Matematica(180-angulo_interior+"°")



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    arco_derecho = Racional(randrange(50, 180, 2))
    arco_izquierdo = Racional(randrange(50, 180, 2))
    angulo_interior = (arco_derecho+arco_izquierdo)/2
    while not 50<angulo_interior<130:
        arco_derecho = Racional(randrange(50, 180, 2))
        arco_izquierdo = Racional(randrange(50, 180, 2))
        angulo_interior = (arco_derecho+arco_izquierdo)/2

    angulo_de_giro = Racional(randrange(0, 360))

    radio = "1.5"

    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura el arco {Matematica("AB")} mide {Matematica(potencia(arco_derecho,"°"))}.
\begin{{center}}
\begin{{tikzpicture}} [scale=1]

\draw (0,0) circle({radio});

\tkzDefPoint(0,0){{O}}
\tkzDefPoint({-arco_derecho/2+angulo_de_giro}:{radio}){{A}}
\tkzDefPoint({arco_derecho/2+angulo_de_giro}:{radio}){{B}}
\tkzDefPoint({180-arco_izquierdo/2+angulo_de_giro}:{radio}){{C}}
\tkzDefPoint({180+arco_izquierdo/2+angulo_de_giro}:{radio}){{D}}
\tkzInterLL(A,C)(B,D) \tkzGetPoint{{P}}

\tkzDrawPoints(A,B,C,D)

\node [label={-arco_derecho/2+angulo_de_giro}:A] at (A){{}};
\node [label={arco_derecho/2+angulo_de_giro}:B] at (B){{}};
\node [label={180-arco_izquierdo/2+angulo_de_giro}:C] at (C){{}};
\node [label={180+arco_izquierdo/2+angulo_de_giro}:D] at (D){{}};

\tkzDrawSegment(A,C)
\tkzDrawSegment(B,D)

\draw pic["{Matematica(potencia(angulo_interior,"°"))}",draw,angle radius=0.7cm] {{{choice(["angle=A--P--B", "angle=C--P--D"])}}};

\end{{tikzpicture}} \end{{center}}
¿Cuánto mide el arco CD?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(arco_izquierdo+"°")
    contenido_2 = Matematica(arco_izquierdo*2+"°")
    contenido_3 = Matematica(Racional(arco_izquierdo,2,True)+"°")
    contenido_4 = Matematica(angulo_interior+"°")
    contenido_5 = Matematica(abs(angulo_interior*2+arco_derecho)*2+"°")







enunciado_oculto = [arco_izquierdo,arco_derecho,opcion]










