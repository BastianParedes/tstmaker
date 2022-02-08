{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
angulo_de_giro = Racional(randrange(0, 360, 2))
angulo_central = Racional(randrange(50, 181, 2))
giro_de_angulo_inscrito = Racional(randrange(-70, 70))
while -10<giro_de_angulo_inscrito-angulo_central/2<10 or -10<giro_de_angulo_inscrito+angulo_central/2<10:
    angulo_central = Racional(randrange(50, 181, 2))
    giro_de_angulo_inscrito = Racional(randrange(-70, 70))



if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura los puntos A, B y C están sobre la circunferencia de centro O y el ángulo AOB mide {Matematica(potencia(angulo_central,"°"))}.
\begin{{center}}
\begin{{tikzpicture}} [scale=1]
\tkzDefPoint(0,0){{O}}
\tkzDefPoint({angulo_de_giro}:2){{A}}
\tkzDefPoint({(angulo_central+angulo_de_giro)%360}:2){{B}}
\tkzDefPoint({(angulo_central/2+180+angulo_de_giro+giro_de_angulo_inscrito)%360}:2){{C}}

\node [label={(angulo_central/2+180+angulo_de_giro)%360}:O] at (O){{}};
\node [label={angulo_de_giro%360}:A] at (A){{}};
\node [label={(angulo_central+angulo_de_giro)%360}:B] at (B){{}};
\node [label={(angulo_central/2+180+angulo_de_giro+giro_de_angulo_inscrito)%360}:C] at (C){{}};

\draw pic["{Matematica(potencia(angulo_central,"°"))}",draw,angle radius=0.8cm] {{angle=A--O--B}};

\draw (0,0) circle(2);

\tkzDrawPoints(O)

\tkzDrawSegment(O,A)
\tkzDrawSegment(O,B)
\tkzDrawSegment(C,A)
\tkzDrawSegment(C,B)

\end{{tikzpicture}} \end{{center}}

¿Cuánto mide el ángulo ACB?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(angulo_central,2,True)+"°")
    contenido_2 = Matematica(angulo_central+"°")
    contenido_3 = Matematica(angulo_central*2+"°")
    contenido_4 = Matematica(angulo_central**2+"°")
    contenido_5 = Matematica(potencia(Root(angulo_central),"°"))



elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura los puntos A, B y C están sobre la circunferencia de centro O y el ángulo ACB mide {Matematica(potencia(angulo_central/2,"°"))}.
\begin{{center}}
\begin{{tikzpicture}} [scale=1]
\tkzDefPoint(0,0){{O}}
\tkzDefPoint({angulo_de_giro}:2){{A}}
\tkzDefPoint({(angulo_central+angulo_de_giro)%360}:2){{B}}
\tkzDefPoint({(angulo_central/2+180+angulo_de_giro+giro_de_angulo_inscrito)%360}:2){{C}}

\node [label={(angulo_central/2+180+angulo_de_giro)%360}:O] at (O){{}};
\node [label={angulo_de_giro%360}:A] at (A){{}};
\node [label={(angulo_central+angulo_de_giro)%360}:B] at (B){{}};
\node [label={(angulo_central/2+180+angulo_de_giro+giro_de_angulo_inscrito)%360}:C] at (C){{}};

\draw pic["{Matematica(potencia(angulo_central/2,"°"))}",draw,angle radius=0.8cm] {{angle=A--C--B}};

\draw (0,0) circle(2);

\tkzDrawPoints(O)

\tkzDrawSegment(O,A)
\tkzDrawSegment(O,B)
\tkzDrawSegment(C,A)
\tkzDrawSegment(C,B)

\end{{tikzpicture}} \end{{center}}

¿Cuánto mide el ángulo AOB?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(angulo_central,2,True)+"°")
    contenido_2 = Matematica(angulo_central+"°")
    contenido_3 = Matematica(angulo_central*2+"°")
    contenido_4 = Matematica(Racional(angulo_central,4,True)+"°")
    contenido_5 = Matematica(potencia(Root(Racional(angulo_central,2,True)),"°"))




enunciado_oculto = angulo_central










