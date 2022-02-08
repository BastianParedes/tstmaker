{"cantidad_opciones":4, "cantidad_disponible":50}

if opcion==1:#Circunferencia, teorema de cuerdas
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    producto_de_soluciones = Natural(randrange(2, 30)**2)
    x1, x2 = Racional(1), Racional(1)
    for primo in producto_de_soluciones.lista_descomposicion_en_primos:
        if choice([1,2])==1:
            x1 = x1*primo
        else:
            x2 = x2*primo
    a, r = Root(x1*x2), Racional(x1+x2,2,True)
    while x1==x2 or type(a)==Root:
        producto_de_soluciones = Natural(randrange(2, 10)**2)
        x1, x2 = Racional(1), Racional(1)
        for primo in producto_de_soluciones.lista_descomposicion_en_primos:
            if choice([1,2])==1:
                x1 = x1*primo
            else:
                x2 = x2*primo
        a, r = Root(x1*x2), Racional(x1+x2,2,True)

    angulo_de_giro = Racional(randrange(0, 360))
    angulo_1 = randrange(45, 75)
    unidad_de_medida = choice(["mm", "cm", "m", "km"])

    lista_de_letras = ["A","B","C","D","E"]
    shuffle(lista_de_letras)
    letra_A, letra_B, letra_C, letra_D, letra_E = lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3], lista_de_letras[4]

    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente circunferencia de centro O se cumple que {Matematica(linea(letra_A+letra_C))} {choice(["es cuerda diametral", "contiene a su centro"])}, {letra_E} es el punto de intersección entre {Matematica(linea(letra_A+letra_C))} y {Matematica(linea(letra_B+letra_D))}, {choice([
Matematica(linea(choice([letra_B+letra_E,letra_D+letra_E])))+" mide "+Matematica(a+" "+unidad_de_medida,arreglar_espacios=True), Matematica(linea(letra_B+letra_D))+" mide "+Matematica(2*a+" "+unidad_de_medida,arreglar_espacios=True)])} y {choice([
Matematica(linea(choice([letra_C+"O",letra_A+"O"])))+" mide "+Matematica(r+" "+unidad_de_medida,arreglar_espacios=True), Matematica(linea(letra_C+letra_A))+" mide "+Matematica(2*r+" "+unidad_de_medida,arreglar_espacios=True)])}
\begin{{center}} \begin{{tikzpicture}} [scale=1.5]

\draw (0,0) circle(1);

\tkzDefPoint({0+angulo_de_giro}:1){{{letra_A}}}
\tkzDefPoint({angulo_1+angulo_de_giro}:1){{{letra_B}}}
\tkzDefPoint({180+angulo_de_giro}:1){{{letra_C}}}
\tkzDefPoint({-angulo_1+angulo_de_giro}:1){{{letra_D}}}
\tkzInterLL({letra_A},{letra_C})({letra_B},{letra_D}) \tkzGetPoint{{{letra_E}}}
\tkzDefPoint(0,0){{O}}

\tkzDrawSegment({letra_A},{letra_C})
\tkzDrawSegment({letra_B},{letra_D})
\tkzDrawPoints[fill=black](O)

\node [label={0+angulo_de_giro}:{letra_A}] at ({letra_A}){{}};
\node [label={angulo_1+angulo_de_giro}:{letra_B}] at ({letra_B}){{}};
\node [label={180+angulo_de_giro}:{letra_C}] at ({letra_C}){{}};
\node [label={-angulo_1+angulo_de_giro}:{letra_D}] at ({letra_D}){{}};
\node [label={choice([135,225])+angulo_de_giro}:O] at (O){{}};

\tkzMarkRightAngle[size={randrange(10,16)/100}]({choice([f"{letra_A},{letra_E},{letra_B}", f"{letra_B},{letra_E},{letra_C}", f"{letra_C},{letra_E},{letra_D}", f"{letra_D},{letra_E},{letra_A}"])})

\end{{tikzpicture}} \end{{center}}
{Matematica(linea(letra_A+letra_E))} mide"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(min(x1,x2))+" "+unidad_de_medida
    contenido_2 = Matematica(max(x1,x2))+" "+unidad_de_medida
    contenido_3 = Matematica(a**2/r)+" "+unidad_de_medida
    contenido_4 = Matematica(Fraction(Pol(r,-Root(abs(r**2-4*a**2)),reducir=True,reducir_raices=False), 2, simplificar=True))+" "+unidad_de_medida
    contenido_5 = Matematica(Fraction(Pol(r,Root(abs(r**2-4*a**2)),reducir=True,reducir_raices=False), 2, simplificar=True))+" "+unidad_de_medida
    enunciado_oculto = [opcion, a, r]






elif opcion==2:#Circunferencia, teorema de secantes
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    x1, x2 = Racional(randrange(2,11)), -Racional(randrange(2,11))
    ea, bc, ed = Racional(1), -x1-x2, Racional(1)
    for primo in Natural(-x1*x2).lista_descomposicion_en_primos:
        if choice([1,2])==1:
            ea = ea*primo
        else:
            ed = ed*primo
    ad = ea-ed
    while not ed<ea or bc<=0 or ad*ea-bc==0:
        x1, x2 = Racional(randrange(2,11)), -Racional(randrange(2,11))
        ea, bc, ed = Racional(1), -x1-x2, Racional(1)
        for primo in Natural(-x1*x2).lista_descomposicion_en_primos:
            if choice([1,2])==1:
                ea = ea*primo
            else:
                ed = ed*primo
        ad = ea-ed

    # A  D
    #       E
    # B  C

    angulo_4 = randrange(10,50)
    angulo_1 = 180-angulo_4-randrange(30, 40)
    angulo_3 = randrange(-45, -10)
    angulo_2 = -180-angulo_3+randrange(20, 30)
    angulo_de_giro = Racional(randrange(0, 360))

    lista_de_letras = ["A","B","C","D","E"]

    letra_A = choice(lista_de_letras)
    lista_de_letras.remove(letra_A)
    letra_B = choice(lista_de_letras)
    lista_de_letras.remove(letra_B)
    letra_C = choice(lista_de_letras)
    lista_de_letras.remove(letra_C)
    letra_D = choice(lista_de_letras)
    lista_de_letras.remove(letra_D)
    letra_E = choice(lista_de_letras)
    lista_de_letras.remove(letra_E)

    letra_A, letra_B, letra_C, letra_D, letra_E = "A", "B", "C", "D", "E"

    unidad_de_medida = choice(["mm", "cm", "m", "km"])

    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura los puntos {Matematica(letra_A)}, {Matematica(letra_B)}, {Matematica(letra_C)} y {Matematica(letra_D)} están sobre la circunferencia
\begin{{center}}
\begin{{tikzpicture}} [scale=1.5]

\draw (0,0) circle(1);

\tkzDefPoint({angulo_1+angulo_de_giro}:1){{{letra_A}}}
\tkzDefPoint({angulo_2+angulo_de_giro}:1){{{letra_B}}}
\tkzDefPoint({angulo_3+angulo_de_giro}:1){{{letra_C}}}
\tkzDefPoint({angulo_4+angulo_de_giro}:1){{{letra_D}}}
\tkzInterLL({letra_B},{letra_C})({letra_A},{letra_D}) \tkzGetPoint{{{letra_E}}}

\tkzDrawSegment({letra_A},{letra_E})
\tkzDrawSegment({letra_B},{letra_E})

\node [label={angulo_1+angulo_de_giro}:{letra_A}] at ({letra_A}){{}};
\node [label={angulo_2+angulo_de_giro}:{letra_B}] at ({letra_B}){{}};
\node [label={angulo_3+angulo_de_giro}:{letra_C}] at ({letra_C}){{}};
\node [label={angulo_4+angulo_de_giro}:{letra_D}] at ({letra_D}){{}};
\node [label={choice([90,270])+angulo_de_giro}:{letra_E}] at ({letra_E}){{}};

\end{{tikzpicture}} \end{{center}}
Si {Matematica(linea(letra_E+letra_D))} mide {Matematica(ed+" "+unidad_de_medida,arreglar_espacios=True)}, {Matematica(linea(letra_E+letra_A))} mide {Matematica(ea+" "+unidad_de_medida,arreglar_espacios=True)} y {Matematica(linea(letra_B+letra_C))} mide {Matematica(bc+" "+unidad_de_medida,arreglar_espacios=True)}, ¿cuánto mide {Matematica(linea(letra_E+letra_C))}?"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x1)+" "+unidad_de_medida
    contenido_2 = Matematica(x2)+" "+unidad_de_medida
    contenido_3 = Matematica(bc/(ad*ed))+" "+unidad_de_medida
    contenido_4 = Matematica(bc/(ad*ea-bc))+" "+unidad_de_medida
    contenido_5 = Matematica(ed*ea/bc)+" "+unidad_de_medida
    enunciado_oculto = [opcion, ea, ed, bc]




elif opcion==3:#Circunferencia, teorema de tangente
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    x1 = Racional(randrange(2,25))
    ec, eb = Racional(1), Racional(1)
    for primo in Natural(x1**2).lista_descomposicion_en_primos:
        if choice([1,2])==1:
            eb = eb*primo
        else:
            ec = ec*primo
    bc = eb-ec
    while bc<=0 or not ec<eb:
        ec, eb = Racional(1), Racional(1)
        for primo in Natural(x1**2).lista_descomposicion_en_primos:
            if choice([1,2])==1:
                eb = eb*primo
            else:
                ec = ec*primo
        bc = eb-ec
    #   A  
    #       E
    # B  C

    lista_de_letras = ["A","B","C","D","E"]

    letra_A = choice(lista_de_letras)
    lista_de_letras.remove(letra_A)
    letra_B = choice(lista_de_letras)
    lista_de_letras.remove(letra_B)
    letra_C = choice(lista_de_letras)
    lista_de_letras.remove(letra_C)
    letra_E = choice(lista_de_letras)
    lista_de_letras.remove(letra_E)

    letra_A, letra_B, letra_C, letra_E = "A", "B", "C", "E"

    unidad_de_medida = choice(["mm", "cm", "m", "km"])

    medidas_de_lados = [f"{Matematica(linea(letra_B+letra_E))} mide {Matematica(eb+' '+unidad_de_medida,arreglar_espacios=True)}", f"{Matematica(linea(letra_C+letra_E))} mide {Matematica(ec+' '+unidad_de_medida,arreglar_espacios=True)}", f"{Matematica(linea(letra_B+letra_C))} mide {Matematica(bc+' '+unidad_de_medida,arreglar_espacios=True)}"]
    shuffle(medidas_de_lados)

    angulo_de_giro = randrange(0, 360)



    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura los puntos {Matematica(letra_A)}, {Matematica(letra_B)} y {Matematica(letra_C)} están sobre la circunferencia, {Matematica(linea(letra_A+letra_E))} es tangente a la circunferencia en {letra_A}, {medidas_de_lados[0]} y {medidas_de_lados[1]}
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate={angulo_de_giro}]
\coordinate (O) at (0,0);
\coordinate [label={90+angulo_de_giro}:{letra_A}] ({letra_A}) at (0,1);
\node (circulo) [draw,circle through=({letra_A})] at (O) {{}};"""
    if choice([1,2])==1:
        enunciado += fr"""
\coordinate [label={225+angulo_de_giro}:{letra_B}] ({letra_B}) at ({randrange(180,270)}:1);
\coordinate [label={randrange(0,90)+angulo_de_giro}:{letra_E}] ({letra_E}) at ({randrange(10,40)/10},1);

\coordinate [label={-45+angulo_de_giro}:{letra_C}] ({letra_C}) at (intersection 1 of circulo and {letra_B}--{letra_E});

\draw ({letra_A})--({letra_E});
\draw ({letra_E})--({letra_B});

\end{{tikzpicture}} \end{{center}}"""

    else:
        enunciado += fr"""
\coordinate [label={-45+angulo_de_giro}:B] (B) at ({180-randrange(180,270)}:1);
\coordinate [label={180-randrange(0,90)+angulo_de_giro}:E] (E) at (-{randrange(10,40)/10},1);

\coordinate [label={225+angulo_de_giro}:C] (C) at (intersection 1 of circulo and B--E);

\draw (A)--(E);
\draw (E)--(B);

\end{{tikzpicture}} \end{{center}}"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x1)+" "+unidad_de_medida
    contenido_2 =        Matematica(ec*eb)+" "+unidad_de_medida
    contenido_3 =        Matematica(eb/choice([ec,bc]))+" "+unidad_de_medida
    contenido_4 =        Matematica(Root(ec*bc))+" "+unidad_de_medida
    contenido_5 =        Matematica(Root(eb*bc))+" "+unidad_de_medida
    enunciado_oculto = [opcion, ec,eb]



elif opcion==4:#Pitágoras, al principio es cuadrática, pero después es lineal
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    unidad_de_medida = choice(["mm", "cm", "m", "km"])
    angulo_de_giro = randrange(0, 360)
    lista_trios = [[3, 4, 5], [6, 8, 10], [9, 12, 15], [5, 12, 13], [8, 15, 17]]
    trio = choice(lista_trios)
    c = Racional(trio[2])
    trio.remove(c.numerador)
    a = Racional(choice(trio))
    trio.remove(a.numerador)
    b = Racional(choice(trio))
    d, e, f = Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0))
    while a*d+b*e-c*f==0 or a*d+b*e+c*f==0 or a+b-c==0:
        d, e, f = Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0))
    x = (f**2-d**2-e**2)/(2*(a*d+b*e-c*f))
    while a*x+d<=0 or c*x+f<=0 or b*x+e<=0:
        d, e, f = Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0))
        while a*d+b*e-c*f==0 or a*d+b*e+c*f==0 or a+b-c==0:
            d, e, f = Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0)), Racional(elegir(-11,11, 0))
        x = (f**2-d**2-e**2)/(2*(a*d+b*e-c*f))
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En un triángulo rectángulo se tiene que un cateto mide {Matematica(Pol(a*"x",d))} cm, el otro mide {Matematica(Pol(b*"x",e))} cm y la hipotenusa mide {Matematica(Pol(c*"x",f))} cm
    \begin{{center}}\begin{{tikzpicture}}  [scale=1, rotate={angulo_de_giro}]
    \coordinate (A) at (0,0);
    \coordinate (B) at ({randrange(15,40)/10},0);
    \coordinate (C) at (0,{randrange(15,40)/10});

    \coordinate [label={270+angulo_de_giro}:{Matematica(Pol(a*"x",d))} {unidad_de_medida}] (AB) at ($(A)!0.5!(B)$);
    \coordinate [label={45+angulo_de_giro}:{Matematica(Pol(c*"x",f))} {unidad_de_medida}] (BC) at ($(B)!0.5!(C)$);
    \coordinate [label={180+angulo_de_giro}:{Matematica(Pol(b*"x",e))} {unidad_de_medida}] (CA) at ($(C)!0.5!(A)$);

    \tkzDrawPolygon(A,B,C)

    \tkzMarkRightAngle(B,A,C)

    \end{{tikzpicture}} \end{{center}}
    El valor de x es"""

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero.=
    contenido_correcto = Matematica((f**2-d**2-e**2)/(2*(a*d+b*e-c*f)))
    contenido_2 = Matematica((f-d-e)/(a+b-c))
    contenido_3 = Matematica(f-d-e)
    contenido_4 = Matematica((f**2-d**2-e**2)/(a*d+b*e-c*f))
    contenido_5 = Matematica((f**2+d**2+e**2)/(2*(a*d+b*e+c*f)))

    enunciado_oculto = [a,b,c,d,e,f]










