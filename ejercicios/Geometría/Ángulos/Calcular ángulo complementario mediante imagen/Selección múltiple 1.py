{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
letra = choice([r"\alpha", r"\beta", r"\gamma"])
angulo_conocido = elegir(30,60)
angulo_de_giro = elegir(0,360)

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""¿Cuál es el valor de ${letra}$?

    \begin{{center}}
    \begin{{tikzpicture}} [scale=1]

    \tkzDefPoint(0,0){{O}}
    \tkzDefPoint({0+angulo_de_giro}:2){{A}}
    \tkzDefPoint({angulo_conocido+angulo_de_giro}:1.5){{B}}
    \tkzDefPoint({90+angulo_de_giro}:2){{C}}

    \tkzDrawPoints(A,B,C)

    \node [label={270+angulo_de_giro}:A] at (A){{}};
    \node [label={90+angulo_conocido+angulo_de_giro}:B] at (B){{}};
    \node [label={180+angulo_de_giro}:C] at (C){{}};

    \tkzDrawSegment[->,add=0 and 0.2](O,A)
    \tkzDrawSegment[->,add=0 and 0.2](O,B)
    \tkzDrawSegment[->,add=0 and 0.2](O,C)

    \draw pic["{Matematica(str(angulo_conocido)+'°')}",draw,angle radius=1.2cm] {{angle=A--O--B}};
    \draw pic["${letra}$",draw,angle radius=0.8cm] {{angle=B--O--C}};
    \tkzMarkRightAngle(A,O,C)

    \end{{tikzpicture}}
    \end{{center}}"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(str(90-angulo_conocido)+"°")
    contenido_2 = Matematica(str(180-angulo_conocido)+"°")
    contenido_3 = Matematica(str(360-angulo_conocido)+"°")
    contenido_4 = Matematica(str(angulo_conocido)+"°")
    contenido_5 = Matematica(str(180)+"°")



elif opcion==2:
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""¿Cuál es el valor de ${letra}$?

    \begin{{center}}
    \begin{{tikzpicture}} [scale=1]

    \tkzDefPoint(0,0){{O}}
    \tkzDefPoint({0+angulo_de_giro}:2){{A}}
    \tkzDefPoint({(90-angulo_conocido)+angulo_de_giro}:1.5){{B}}
    \tkzDefPoint({90+angulo_de_giro}:2){{C}}

    \tkzDrawPoints(A,B,C)

    \node [label={270+angulo_de_giro}:A] at (A){{}};
    \node [label={90+angulo_conocido+angulo_de_giro}:B] at (B){{}};
    \node [label={180+angulo_de_giro}:C] at (C){{}};

    \tkzDrawSegment[->,add=0 and 0.2](O,A)
    \tkzDrawSegment[->,add=0 and 0.2](O,B)
    \tkzDrawSegment[->,add=0 and 0.2](O,C)

    \draw pic["{Matematica(str(angulo_conocido)+'°')}",draw,angle radius=1.2cm] {{angle=B--O--C}};
    \draw pic["${letra}$",draw,angle radius=0.8cm] {{angle=A--O--B}};
    \tkzMarkRightAngle(A,O,C)

    \end{{tikzpicture}}
    \end{{center}}"""


if angulo_conocido==45:
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(str(45)+"°")
    contenido_2 = Matematica(str(135)+"°")
    contenido_3 = Matematica(str(315)+"°")
    contenido_4 = Matematica(str(180)+"°")
    contenido_5 = Matematica(str(360)+"°")

else:
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(str(90-angulo_conocido)+"°")
    contenido_2 = Matematica(str(180-angulo_conocido)+"°")
    contenido_3 = Matematica(str(360-angulo_conocido)+"°")
    contenido_4 = Matematica(str(angulo_conocido)+"°")
    contenido_5 = Matematica(str(180)+"°")




enunciado_oculto = [angulo_conocido,opcion]










