{"cantidad_opciones":3, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    arco_derecho = Racional(randrange(40, 180, 2))
    arco_izquierdo = Racional(randrange(40, 180, 2))
    angulo_exterior = (arco_derecho-arco_izquierdo)/2
    while not 30<angulo_exterior<60 or not arco_izquierdo<arco_derecho:
        arco_derecho = Racional(randrange(40, 180, 2))
        arco_izquierdo = Racional(randrange(40, 180, 2))
        angulo_exterior = (arco_derecho-arco_izquierdo)/2

    angulo_de_giro = Racional(choice(range(-20, 21))+choice([0,180]))

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
\tkzInterLL(B,C)(A,D) \tkzGetPoint{{P}}

\tkzDrawPoints(A,B,C,D)

\node [label={-arco_derecho/2+angulo_de_giro}:A] at (A){{}};
\node [label={arco_derecho/2+angulo_de_giro}:B] at (B){{}};
\node [label={180-arco_izquierdo/2+angulo_de_giro}:C] at (C){{}};
\node [label={180+arco_izquierdo/2+angulo_de_giro}:D] at (D){{}};

\tkzDrawSegment(P,B)
\tkzDrawSegment(P,A)

\draw pic["$\alpha$",draw,angle radius=0.7cm] {{angle=A--P--B}};

\end{{tikzpicture}} \end{{center}}
¿Cuál es el valor de $\alpha$?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(angulo_exterior+"°")
    contenido_2 = Matematica(angulo_exterior*2+"°")
    contenido_3 = Matematica(Racional(arco_izquierdo+arco_derecho,2,True)+"°")
    contenido_4 = Matematica(arco_izquierdo+arco_derecho+"°")
    contenido_5 = Matematica(180-angulo_exterior+"°")



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    arco_derecho = Racional(randrange(40, 180, 2))
    arco_izquierdo = Racional(randrange(40, 180, 2))
    angulo_exterior = (arco_derecho-arco_izquierdo)/2
    while not 40<angulo_exterior<60 or not arco_izquierdo<arco_derecho:
        arco_derecho = Racional(randrange(40, 180, 2))
        arco_izquierdo = Racional(randrange(40, 180, 2))
        angulo_exterior = (arco_derecho-arco_izquierdo)/2

    angulo_de_giro = Racional(choice(range(-20, 21))+choice([0,180]))

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
\tkzInterLL(B,C)(A,D) \tkzGetPoint{{P}}

\tkzDrawPoints(A,B,C,D)

\node [label={-arco_derecho/2+angulo_de_giro}:A] at (A){{}};
\node [label={arco_derecho/2+angulo_de_giro}:B] at (B){{}};
\node [label={180-arco_izquierdo/2+angulo_de_giro}:C] at (C){{}};
\node [label={180+arco_izquierdo/2+angulo_de_giro}:D] at (D){{}};

\tkzDrawSegment(P,B)
\tkzDrawSegment(P,A)

\draw pic["{Matematica(potencia(angulo_exterior,"°"))}",draw,angle radius=0.7cm] {{angle=A--P--B}};

\end{{tikzpicture}} \end{{center}}
¿Cuánto mide el arco {Matematica("CD")}?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(arco_izquierdo+"°")
    contenido_2 = Matematica(arco_izquierdo*2+"°")
    contenido_3 = Matematica(Racional(arco_izquierdo,2,True)+"°")
    contenido_4 = Matematica(Racional(arco_derecho+angulo_exterior,2,True)+"°")
    contenido_5 = Matematica(Racional(abs(arco_derecho-angulo_exterior),2,True)+"°")





elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    arco_derecho = Racional(randrange(40, 180, 2))
    arco_izquierdo = Racional(randrange(40, 180, 2))
    angulo_exterior = (arco_derecho-arco_izquierdo)/2
    while not 40<angulo_exterior<60 or not arco_izquierdo<arco_derecho:
        arco_derecho = Racional(randrange(40, 180, 2))
        arco_izquierdo = Racional(randrange(40, 180, 2))
        angulo_exterior = (arco_derecho-arco_izquierdo)/2

    angulo_de_giro = Racional(choice(range(-20, 21))+choice([0,180]))

    radio = "1.5"

    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura el arco {Matematica("CD")} mide {Matematica(potencia(arco_izquierdo,"°"))}.
\begin{{center}}
\begin{{tikzpicture}} [scale=1]

\draw (0,0) circle({radio});

\tkzDefPoint(0,0){{O}}
\tkzDefPoint({-arco_derecho/2+angulo_de_giro}:{radio}){{A}}
\tkzDefPoint({arco_derecho/2+angulo_de_giro}:{radio}){{B}}
\tkzDefPoint({180-arco_izquierdo/2+angulo_de_giro}:{radio}){{C}}
\tkzDefPoint({180+arco_izquierdo/2+angulo_de_giro}:{radio}){{D}}
\tkzInterLL(B,C)(A,D) \tkzGetPoint{{P}}

\tkzDrawPoints(A,B,C,D)

\node [label={-arco_derecho/2+angulo_de_giro}:A] at (A){{}};
\node [label={arco_derecho/2+angulo_de_giro}:B] at (B){{}};
\node [label={180-arco_izquierdo/2+angulo_de_giro}:C] at (C){{}};
\node [label={180+arco_izquierdo/2+angulo_de_giro}:D] at (D){{}};

\tkzDrawSegment(P,B)
\tkzDrawSegment(P,A)

\draw pic["{Matematica(potencia(angulo_exterior,"°"))}",draw,angle radius=0.7cm] {{angle=A--P--B}};

\end{{tikzpicture}} \end{{center}}
¿Cuánto mide el arco {Matematica("AB")}?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(arco_derecho+"°")
    contenido_2 = Matematica(arco_derecho*2+"°")
    contenido_3 = Matematica(Racional(arco_derecho,2,True)+"°")
    contenido_4 = Matematica(Racional(arco_izquierdo+angulo_exterior,2,True)+"°")
    contenido_5 = Matematica(Racional(abs(arco_izquierdo-angulo_exterior),2,True)+"°")




enunciado_oculto = [arco_izquierdo,arco_derecho,opcion]











