{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
angulo_4 = randrange(10,50)
angulo_1 = 180-angulo_4-randrange(30, 40)
angulo_3 = randrange(-45, -10)
angulo_2 = -180-angulo_3+randrange(20, 30)
angulo_de_giro = randrange(0,360)
# E - C - B
# E - D - A

unidad_de_medida = choice(["mm", "cm", "m", "km"])
ED = Racional(randrange(1,10))
DA = Racional(randrange(1,10))
EA = ED+DA
lista_del_otro_lado = [Matematica(linea("ED"))+" mide "+Matematica(ED+" "+unidad_de_medida), Matematica(linea("DA"))+" mide "+Matematica(DA+" "+unidad_de_medida), Matematica(linea("EA"))+" mide "+Matematica(EA+" "+unidad_de_medida)]
shuffle(lista_del_otro_lado)


if opcion==1:#Pide EB
    EC = Racional(randrange(1,10))
    EB = ED*EA/EC
    CB = abs(EB-EC)
    lista_de_lados = [lista_del_otro_lado[0], lista_del_otro_lado[1], Matematica(linea("EC"))+" mide "+Matematica(EC+" "+unidad_de_medida)]
    shuffle(lista_de_lados)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente circunferencia se cumple que {lista_de_lados[0]}, {lista_de_lados[1]} y {lista_de_lados[2]}
    \begin{{center}}
    \begin{{tikzpicture}} [scale=1.6]

    \draw (0,0) circle(1);

    \tkzDefPoint(0,0){{O}}
    \tkzDefPoint({angulo_1+angulo_de_giro}:1){{A}}
    \tkzDefPoint({angulo_2+angulo_de_giro}:1){{B}}
    \tkzDefPoint({angulo_3+angulo_de_giro}:1){{C}}
    \tkzDefPoint({angulo_4+angulo_de_giro}:1){{D}}
    \tkzInterLL(B,C)(A,D) \tkzGetPoint{{E}}

    \tkzDrawPoints(A,B,E)

    \node [label={angulo_1+angulo_de_giro}:A] at (A){{}};
    \node [label={angulo_2+angulo_de_giro}:B] at (B){{}};
    \node [label={angulo_3+angulo_de_giro}:C] at (C){{}};
    \node [label={angulo_4+angulo_de_giro}:D] at (D){{}};
    \node [label={choice([90,270])+angulo_de_giro}:E] at (E){{}};

    \tkzDrawSegment(E,B)
    \tkzDrawSegment(E,A)

    \end{{tikzpicture}} \end{{center}}
    {Matematica(linea("EB"))} mide"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(EB+" "+unidad_de_medida)
    contenido_2 = Matematica(CB+" "+unidad_de_medida)
    contenido_3 = Matematica(ED*DA/EC+" "+unidad_de_medida)
    contenido_4 = Matematica(EC+ED*DA/EC+" "+unidad_de_medida)
    contenido_5 = Matematica(Fraction(Pol(-EC, Root(EC**2-4*(-ED*DA-DA**2)), reducir=True), 2)+" "+unidad_de_medida)



elif opcion==2:#Pide EC
    EB = Racional(randrange(1,10))
    EC = EA*ED/EB
    CB = abs(EB-EC)
    while CB==0:
        EB = Racional(randrange(1,10))
        EC = EA*ED/EB
        CB = abs(EB-EC)
    lista_de_lados = [lista_del_otro_lado[0], lista_del_otro_lado[1], Matematica(linea("EB"))+" mide "+Matematica(EB+" "+unidad_de_medida)]
    shuffle(lista_de_lados)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente circunferencia se cumple que {lista_de_lados[0]}, {lista_de_lados[1]} y {lista_de_lados[2]}
    \begin{{center}}
    \begin{{tikzpicture}} [scale=1.6]

    \draw (0,0) circle(1);

    \tkzDefPoint(0,0){{O}}
    \tkzDefPoint({angulo_1+angulo_de_giro}:1){{A}}
    \tkzDefPoint({angulo_2+angulo_de_giro}:1){{B}}
    \tkzDefPoint({angulo_3+angulo_de_giro}:1){{C}}
    \tkzDefPoint({angulo_4+angulo_de_giro}:1){{D}}
    \tkzInterLL(B,C)(A,D) \tkzGetPoint{{E}}

    \tkzDrawPoints(A,B,E)

    \node [label={angulo_1+angulo_de_giro}:A] at (A){{}};
    \node [label={angulo_2+angulo_de_giro}:B] at (B){{}};
    \node [label={angulo_3+angulo_de_giro}:C] at (C){{}};
    \node [label={angulo_4+angulo_de_giro}:D] at (D){{}};
    \node [label={choice([90,270])+angulo_de_giro}:E] at (E){{}};

    \tkzDrawSegment(E,B)
    \tkzDrawSegment(E,A)

    \end{{tikzpicture}} \end{{center}}
    {Matematica(linea("EC"))} mide"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(EC+" "+unidad_de_medida)
    contenido_2 = Matematica(CB+" "+unidad_de_medida)
    contenido_3 = Matematica(ED*DA/CB+" "+unidad_de_medida)
    contenido_4 = Matematica(ED+" "+unidad_de_medida)
    contenido_5 = Matematica(EC*ED/EA+" "+unidad_de_medida)



enunciado_oculto = [opcion, ED, DA, EC]











