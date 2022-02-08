{"cantidad_opciones":14, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(20,40))
    angulo_dibujo_1 = randrange(20,30)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = "En la siguiente figura se cumple "+Matematica(linea("AB")+r"\cong"+linea("BC"))+fr""" y O es centro de la circunferencia, además {Matematica(linea("AB")+"//"+linea("DE"))}
    \begin{{center}} \begin{{tikzpicture}} [scale=1.5]
    \draw (0,0) circle(1);

    \tkzDefPoint({180-angulo_dibujo_1+angulo_de_giro}:1){{A}}
    \tkzDefPoint({angulo_dibujo_1+angulo_de_giro}:1){{B}}
    \tkzDefPointBy[rotation=center B angle {180-2*angulo_dibujo_1}](A) \tkzGetPoint{{C}}
    \tkzDefPoint({180+angulo_dibujo_1+angulo_de_giro}:1){{D}}
    \tkzDefPoint({-angulo_dibujo_1+angulo_de_giro}:1){{E}}
    \tkzDefPoint(0,0){{O}}

    \tkzDrawSegment(O,D)
    \tkzDrawSegment(A,B)
    \tkzDrawSegment(D,E)
    \tkzDrawSegment(A,C)
    \tkzDrawSegment(B,C)

    \tkzDrawPoints[fill=black](A,B,C,D,E,O)

    \node [label={180-angulo_dibujo_1+angulo_de_giro}:A] at (A){{}};
    \node [label={angulo_dibujo_1+angulo_de_giro}:B] at (B){{}};
    \node [label={-45+angulo_de_giro}:C] at (C){{}};
    \node [label={180+angulo_dibujo_1+angulo_de_giro}:D] at (D){{}};
    \node [label={-angulo_dibujo_1-45+angulo_de_giro}:E] at (E){{}};
    \node [label={angulo_dibujo_1+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.7cm] {{angle=A--O--D}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=1.3cm] {{angle=B--C--A}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(angulo*2+"°")
    contenido_2 = Matematica(Racional(angulo,2,True)+"°")
    contenido_3 = Matematica(Racional(angulo,4,True)+"°")
    contenido_4 = Matematica(angulo*4+"°")
    contenido_5 = Matematica(angulo+"°")



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(15,40))
    angulo_dibujo_1 = randrange(110,130)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = "En la siguiente figura, se tiene un semicírculo de centro O y "+Matematica(r"\angle BAC="+angulo+"°",arreglar_espacios=False)+fr"""
    \begin{{center}} \begin{{tikzpicture}} [scale=2.5]

    \tkzDefPoint({180+angulo_de_giro}:1){{A}}
    \tkzDefPoint({0+angulo_de_giro}:1){{B}}
    \tkzDefPoint({2*angulo_dibujo_1-180++angulo_de_giro}:1){{C}}
    \tkzDefPoint({angulo_dibujo_1++angulo_de_giro}:1){{D}}
    \tkzDefPoint(0,0){{O}}
    \tkzInterLL(A,C)(O,D) \tkzGetPoint{{E}}

    \tkzDrawArc(O,B)(A)

    \tkzDrawSegment(A,C)
    \tkzDrawSegment(O,D)
    \tkzDrawSegment(C,B)
    \tkzDrawSegment(A,B)
    \tkzDrawSegment(D,B)

    \tkzDrawPoints[fill=black](A,B,C,D,O)

    \node [label={180+angulo_de_giro}:A] at (A){{}};
    \node [label={0+angulo_de_giro}:B] at (B){{}};
    \node [label={2*angulo_dibujo_1-180+angulo_de_giro}:C] at (C){{}};
    \node [label={angulo_dibujo_1+angulo_de_giro}:D] at (D){{}};
    \node [label={270+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=1cm] {{angle=C--B--D}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=1cm] {{angle=B--A--C}};
    \tkzMarkRightAngle[size=0.1](C,E,D)
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(90-angulo,2,True)+"°")
    contenido_2 = Matematica(180-angulo+"°")
    contenido_3 = Matematica(90+angulo+"°")
    contenido_4 = Matematica(2*(90-angulo)+"°")
    contenido_5 = Matematica(90-angulo+"°")



elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(10,30))
    angulo_dibujo_1 = randrange(125,150)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura, {Matematica(sub("O",1))} y {Matematica(sub("O",2))} son los centros de las circunferencias. En el triángulo ABC, """+Matematica(r"\angle BAC="+angulo+"°",arreglar_espacios=False)+fr"""
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({randrange(160,170)+angulo_de_giro}:1){{O1}}
    \tkzDefPoint(0,0){{O2}}
    \tkzDefPoint({0+angulo_de_giro}:1){{B}}

    \draw (O1) circle(1);
    \draw (O2) circle(1);
    
    \tkzInterLC(B,O2)(O1,O2) \tkzGetSecondPoint{{A}}
    \tkzInterLC(A,O1)(O2,O1) \tkzGetSecondPoint{{C}}
    
    \tkzDrawPolygon(A,B,C)
    \tkzDrawPoints[fill=black](O1,O2,B,A,C)
    
    \node [label={180+angulo_de_giro}:A] at (A){{}};
    \node [label={0+angulo_de_giro}:B] at (B){{}};
    \node [label={45+angulo_de_giro}:C] at (C){{}};
    \node [label={135+angulo_de_giro}:{Matematica(sub("O",1))}] at (O1){{}};
    \node [label={-45+angulo_de_giro}:{Matematica(sub("O",2))}] at (O2){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.5cm] {{angle=C--B--A}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(180-3*angulo,2,True)+"°")
    contenido_2 = Matematica(Racional((180-3*angulo)*2,True)+"°")
    contenido_3 = Matematica(Racional(180-3*angulo,1,True)+"°")
    contenido_4 = Matematica(180-4*angulo+"°")
    contenido_5 = Matematica(2*angulo+"°")



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(30,60))
    angulo_dibujo_1 = randrange(80,110)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura, O es centro de la circunferencia, el triángulo ABC está inscrito en la figura y {Matematica(linea("AB"))} es diámetro
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({angulo_dibujo_1+180+angulo_de_giro}:1){{A}}
    \tkzDefPoint({angulo_dibujo_1+angulo_de_giro}:1){{B}}
    \tkzDefPoint(0,0){{O}}
    \tkzDefPoint({angulo_de_giro}:1){{C}}

    \draw (O) circle(1);
    
    \tkzDrawPolygon(A,B,C)
    \tkzDrawSegment(O,C)
    \tkzDrawPoints[fill=black](A,B,C,O)
    
    \node [label={angulo_dibujo_1+180+angulo_de_giro}:A] at (A){{}};
    \node [label={angulo_dibujo_1+angulo_de_giro}:B] at (B){{}};
    \node [label={angulo_de_giro}:C] at (C){{}};
    \node [label={angulo_dibujo_1+90+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.7cm] {{angle=C--A--B}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=1cm] {{angle=B--C--O}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(90-angulo+"°")
    contenido_2 = Matematica(180-angulo+"°")
    contenido_3 = Matematica(Racional(90-angulo,2,True)+"°")
    contenido_4 = Matematica(2*(90-angulo)+"°")
    contenido_5 = Matematica(4*(90-angulo)+"°")




elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(30,50))
    angulo_dibujo_1 = randrange(50,65)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = "En la siguiente figura se tiene una semicircunferencia de centro O, "+Matematica(fr"\angle COB={angulo}°",arreglar_espacios=False)+fr""" y el triángulo ADE es isóceles de base AD
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({180+angulo_de_giro}:1){{A}}
    \tkzDefPoint({180-angulo_dibujo_1+angulo_de_giro}:1){{B}}
    \tkzDefPoint({angulo_dibujo_1+angulo_de_giro}:1){{C}}
    \tkzDefPoint({angulo_de_giro}:1){{D}}
    \tkzInterLL(A,B)(D,C) \tkzGetPoint{{E}}
    \tkzDefPoint(0,0){{O}}

    \tkzDrawArc(O,D)(A)    
    \tkzDrawPolygon(A,D,E)
    \tkzDrawSegment(O,B)
    \tkzDrawSegment(O,C)
    \tkzDrawPoints[fill=black](A,B,C,D,E,O)
    
    \node [label={270+angulo_de_giro}:A] at (A){{}};
    \node [label={135+angulo_de_giro}:B] at (B){{}};
    \node [label={45+angulo_de_giro}:C] at (C){{}};
    \node [label={270+angulo_de_giro}:D] at (D){{}};
    \node [label={randrange(0,180)+angulo_de_giro}:E] at (E){{}};
    \node [label={270+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.7cm] {{angle=A--E--D}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=1cm] {{angle=C--O--B}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(180-angulo,2,True)+"°")
    contenido_2 = Matematica(Racional(180-2*angulo,2,True)+"°")
    contenido_3 = Matematica(Racional(180-angulo/2,2,True)+"°")
    contenido_4 = Matematica(180-angulo+"°")
    contenido_5 = Matematica(360-angulo+"°")



elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(elegir(135,270, 180))
    angulo_dibujo_1 = randrange(50,65)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = "En la siguiente figura se tiene una semicircunferencia de centro O, "+Matematica(fr"\angle AOC={angulo}°",arreglar_espacios=False)+fr""" 
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({0+angulo_de_giro}:1){{A}}
    \tkzDefPoint({randrange(int(angulo/3),int(angulo*2/3))+angulo_de_giro}:1){{B}}
    \tkzDefPoint({angulo+angulo_de_giro}:1){{C}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,C,O)
    \tkzDrawPoints[fill=black](A,B,C,O)
    
    \node [label={angulo_de_giro}:A] at (A){{}};
    \node [label={90+angulo_de_giro}:B] at (B){{}};
    \node [label={180+angulo_de_giro}:C] at (C){{}};
    \node [label={270+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.7cm] {{angle=C--B--A}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=0.6cm] {{angle=A--O--C}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(360-angulo,2,True)+"°")
    contenido_2 = Matematica(360-angulo+"°")
    contenido_3 = Matematica(2*(360-angulo)+"°")
    contenido_4 = Matematica(Racional(180-angulo,2,True)+"°")
    contenido_5 = Matematica(180-angulo+"°")


elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(elegir(45,135, 90))
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura, {Matematica(linea("AB"))} es cuerda diametral y O es el centro
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({180+angulo_de_giro}:1){{A}}
    \tkzDefPoint({0+angulo_de_giro}:1){{B}}
    \tkzDefPoint({angulo+angulo_de_giro}:1){{C}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,C)
    \tkzDrawSegment(O,C)
    \tkzDrawPoints[fill=black](A,B,C,O)
    
    \node [label={180+angulo_de_giro}:A] at (A){{}};
    \node [label={0+angulo_de_giro}:B] at (B){{}};
    \node [label={90+angulo_de_giro}:C] at (C){{}};
    \node [label={270+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.7cm] {{angle=B--O--C}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=0.6cm] {{angle=B--A--C}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(angulo,2,True)+"°")
    contenido_2 = Matematica(angulo+"°")
    contenido_3 = Matematica(2*angulo+"°")
    contenido_4 = Matematica(180-angulo+"°")
    contenido_5 = Matematica(360-angulo+"°")




elif opcion==7:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(30,60))
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura, {Matematica(linea("AB"))} es cuerda diametral de la circunferencia de centro O
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({180+angulo_de_giro}:1){{A}}
    \tkzDefPoint({0+angulo_de_giro}:1){{B}}
    \tkzDefPoint({2*angulo+angulo_de_giro}:1){{C}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,C)
    \tkzDrawPoints[fill=black](A,B,C,O)
    
    \node [label={180+angulo_de_giro}:A] at (A){{}};
    \node [label={0+angulo_de_giro}:B] at (B){{}};
    \node [label={2*angulo+angulo_de_giro}:C] at (C){{}};
    \node [label={270+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=1cm] {{angle=C--B--A}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=1cm] {{angle=B--A--C}};
    
    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(90-angulo+"°")
    contenido_2 = Matematica(180-angulo+"°")
    contenido_3 = Matematica("90°")
    contenido_4 = Matematica(Racional(90-angulo,2,True)+"°")
    contenido_5 = Matematica(2*(90-angulo)+"°")




elif opcion==8:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo = Racional(randrange(30,60))
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente figura, "+Matematica(r"\angle ACB="+angulo+"°",arreglar_espacios=False)+fr""" y O es el centro de la circunferencia
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({randrange(200,220)+angulo_de_giro}:1){{A}}
    \tkzDefPoint({randrange(-45,-35)+angulo_de_giro}:1){{B}}
    \tkzDefPoint({randrange(80,100)+angulo_de_giro}:1){{C}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,C)
    \tkzDrawSegment(O,A)
    \tkzDrawSegment(O,B)
    \tkzDrawPoints[fill=black](A,B,C,O)
    
    \node [label={225+angulo_de_giro}:A] at (A){{}};
    \node [label={-45+angulo_de_giro}:B] at (B){{}};
    \node [label={90+angulo_de_giro}:C] at (C){{}};
    \node [label={90+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.7cm] {{angle=B--A--O}};
    \draw pic["{Matematica(angulo+"°")}",draw,-,angle radius=0.6cm] {{angle=A--C--B}};

    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(90-angulo+"°")
    contenido_2 = Matematica(180-2*angulo+"°")
    contenido_3 = Matematica(180-angulo+"°")
    contenido_4 = Matematica(abs(90-2*angulo)+"°")
    contenido_5 = Matematica(360-2*angulo+"°")




elif opcion==9:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo_1 = Racional(randrange(30,60))
    angulo_2 = Racional(randrange(30,60))
    angulo_dibujo_1 = randrange(40,50)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = fr"""En la siguiente figura, la recta AB es tangente en A a la circunferencia circunscrita al triángulo ACD
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({270+angulo_de_giro}:1){{A}}
    \tkzDefPoint(0,0){{O}}
    \tkzDefTriangle[two angles= {angulo_dibujo_1} and 90](O,A) \tkzGetPoint{{B}};
    \tkzDefPoint({randrange(-20,70)+angulo_de_giro}:1){{C}}
    \tkzDefPoint({randrange(110,210)+angulo_de_giro}:1){{D}}
    \tkzDefTriangle[two angles= {angulo_dibujo_1+5} and 90](O,A) \tkzGetPoint{{E}};
    \tkzDefTriangle[two angles= 90 and {randrange(25,35)}](A,O) \tkzGetPoint{{F}};

    \draw (O) circle(1);
    \tkzDrawPolygon(A,C,D)
    \tkzDrawSegment[<->](E,F)
    \tkzDrawPoints[fill=black](A,B,C,D)
    
    \node [label={270+angulo_de_giro}:A] at (A){{}};
    \node [label={270+angulo_de_giro}:B] at (B){{}};
    \node [label={0+angulo_de_giro}:C] at (C){{}};
    \node [label={180+angulo_de_giro}:D] at (D){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.8cm] {{angle=C--A--D}};
    \draw pic["{Matematica(angulo_1+"°")}",draw,-,angle radius=1cm] {{angle=B--A--C}};
    \draw pic["{Matematica(angulo_2+"°")}",draw,-,angle radius=1cm] {{angle=D--C--A}};

    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(180-angulo_1-angulo_2+"°")
    contenido_2 = Matematica(Racional(180-angulo_1*2-angulo_2,cargar_decimal=True)+"°")
    contenido_3 = Matematica(Racional(180-angulo_1/2-angulo_2,cargar_decimal=True)+"°")
    contenido_4 = Matematica(2*angulo_1+"°")
    contenido_5 = Matematica(Racional(angulo_1,2,cargar_decimal=True)+"°")



elif opcion==10:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo_1 = Racional(randrange(45,65))
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente figura O es el centro de la circunferencia, "+Matematica(Fr"\angle OBA={angulo_1}°",arreglar_espacios=False)+fr""" y {Matematica(linea("AC"))} es una cuerda diámetral
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({90+angulo_de_giro}:1){{A}}
    \tkzDefPoint({180-2*angulo_1+90+angulo_de_giro}:1){{B}}
    \tkzDefPoint({270+angulo_de_giro}:1){{C}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,O)
    \tkzDrawSegment[-](O,C)
    \tkzDrawPoints[fill=black](A,B,C,O)
    
    \node [label={90+angulo_de_giro}:A] at (A){{}};
    \node [label={180-2*angulo_1+90+angulo_de_giro}:B] at (B){{}};
    \node [label={270+angulo_de_giro}:C] at (C){{}};
    \node [label={0+angulo_de_giro}:O] at (O){{}};

    \draw pic["${letra}$",draw,-,angle radius=0.8cm] {{angle=B--O--C}};
    \draw pic["{Matematica(angulo_1+"°")}",draw,-,angle radius=1cm] {{angle=O--B--A}};

    \end{{tikzpicture}} \end{{center}}
    El ángulo ${letra}$ mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(2*angulo_1)
    contenido_2 = Matematica(Racional(angulo_1/2,cargar_decimal=True)+"°")
    contenido_3 = Matematica(90-angulo_1)
    contenido_4 = Matematica(180-angulo_1)
    contenido_5 = Matematica(Racional(180-angulo_1/2,cargar_decimal=True)+"°")



elif opcion==11:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo_1 = Racional(randrange(45,65))
    angulo_2 = angulo_1-randrange(10,20)
    angulo_de_giro = randrange(0,360)
    letra = choice([r"\alpha", r"\beta", r"\delta"])
    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente circunferencia, "+Matematica(Fr"\angle CAE={angulo_1}°",arreglar_espacios=False)+" y "+Matematica(Fr"\angle DBE={angulo_2}°",arreglar_espacios=False)+fr"""
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({randrange(170,190)+angulo_de_giro}:1){{A}}
    \tkzDefPoint({randrange(210,270)+angulo_de_giro}:1){{B}}
    \tkzDefPoint({randrange(-50,-30)+angulo_de_giro}:1){{C}}
    \tkzDefPoint({randrange(-10,10)+angulo_de_giro}:1){{D}}
    \tkzDefPoint({randrange(45,60)+angulo_de_giro}:1){{E}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawSegment[-](A,E)
    \tkzDrawSegment[-](A,C)
    \tkzDrawSegment[-](B,E)
    \tkzDrawSegment[-](B,D)

    \node [label={180+angulo_de_giro}:A] at (A){{}};
    \node [label={225+angulo_de_giro}:B] at (B){{}};
    \node [label={-45+angulo_de_giro}:C] at (C){{}};
    \node [label={0+angulo_de_giro}:D] at (D){{}};
    \node [label={45+angulo_de_giro}:E] at (E){{}};

    \draw pic["{Matematica(angulo_1+"°")}",draw,-,angle radius=1cm] {{angle=C--A--E}};
    \draw pic["{Matematica(angulo_2+"°")}",draw,-,angle radius=1.3cm] {{angle=D--B--E}};

    \end{{tikzpicture}} \end{{center}}
    El arco CD mide"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(2*angulo_1-2*angulo_2+"°")
    contenido_2 = Matematica(angulo_1-angulo_2+"°")
    contenido_3 = Matematica(Racional(angulo_1/2-angulo_2/2,cargar_decimal=True)+"°")
    contenido_4 = Matematica(Racional(angulo_1*2-angulo_2/2,cargar_decimal=True)+"°")
    contenido_5 = Matematica(Racional(abs(angulo_1/2-angulo_2*2),cargar_decimal=True)+"°")



elif opcion==12:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo_1 = Racional(randrange(45,65))
    angulo_2 = angulo_1-randrange(10,20)
    angulo_de_giro = randrange(0,360)
    letras = [r"\alpha", r"\beta", r"\delta"]
    shuffle(letras)
    letra_A, letra_B, letra_C = letras[0], letras[1], letras[2]
    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente circunferencia, {Matematica(linea('AC'))} es cuerda diametral, "+Matematica(Fr"\angle DBA={angulo_1}°",arreglar_espacios=False)+" y "+Matematica(Fr"\angle ACB={angulo_2}°",arreglar_espacios=False)+fr"""
    \begin{{center}} \begin{{tikzpicture}} [scale=2.5]

    \tkzDefPoint({180+angulo_de_giro}:1){{A}}
    \tkzDefPoint({randrange(225,265)+angulo_de_giro}:1){{B}}
    \tkzDefPoint({0+angulo_de_giro}:1){{C}}
    \tkzDefPoint({randrange(95,135)+angulo_de_giro}:1){{D}}
    \tkzDefPoint(0,0){{O}}

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,C,D)
    \tkzDrawSegment[-](A,C)
    \tkzDrawSegment[-](D,B)

    \node [label={180+angulo_de_giro}:A] at (A){{}};
    \node [label={225+angulo_de_giro}:B] at (B){{}};
    \node [label={-45+angulo_de_giro}:C] at (C){{}};
    \node [label={45+angulo_de_giro}:D] at (D){{}};

    \draw pic["${letra_A}$",draw,-,angle radius=0.8cm, dashed] {{angle=D--C--A}};
    \draw pic["${letra_B}$",draw,-,angle radius=0.6cm, dashed] {{angle=A--D--C}};
    \draw pic["${letra_C}$",draw,-,angle radius=0.6cm, dashed] {{angle=B--A--D}};
    \draw pic["{Matematica(angulo_1+"°")}",draw,-,angle radius=1cm] {{angle=D--B--A}};
    \draw pic["{Matematica(angulo_2+"°")}",draw,-,angle radius=1.3cm] {{angle=A--C--B}};

    \end{{tikzpicture}} \end{{center}}
    {Matematica(letra_A+"+"+letra_B+"-"+letra_C+"=")}"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(angulo_1+90-(180-angulo_1-angulo_2)+"°")
    contenido_2 = Matematica(angulo_1+"°")
    contenido_3 = Matematica("90°")
    contenido_4 = Matematica(180-angulo_1-angulo_2+"°")
    contenido_5 = Matematica(abs(angulo_1+90-360-2*angulo_1-2*angulo_2)%360+"°")



elif opcion==13:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo_1 = Racional(randrange(30,60))
    angulo_2 = Racional(randrange(30,60))
    angulo_de_giro = randrange(0,360)
    letras = [r"\alpha", r"\beta", r"\delta"]
    shuffle(letras)
    letra_A, letra_B = letras[0], letras[1]

    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente figura, la recta CD es tangente en C a la circunferencia circunscrita, el arco BC mide {Matematica(angulo_1+'°')} y "+Matematica(Fr"\angle CBA={angulo_2}°",arreglar_espacios=False)+fr"""
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \tkzDefPoint({randrange(-10,25)+angulo_de_giro}:1){{A}}
    \tkzDefPoint({randrange(135,190)+angulo_de_giro}:1){{B}}
    \tkzDefPoint({270+angulo_de_giro}:1){{C}}
    \tkzDefPoint(0,0){{O}}
    \tkzDefTriangle[two angles= {randrange(30,40)} and 90](O,C) \tkzGetPoint{{D}};
    \tkzDefTriangle[two angles= 45 and 90](O,C) \tkzGetPoint{{D2}};
    \tkzDefTriangle[two angles= 90 and {randrange(25,50)}](C,O) \tkzGetPoint{{E}};

    \draw (O) circle(1);
    \tkzDrawPolygon(A,B,C)
    \tkzDrawSegment[<->](E,D2)
    \tkzDrawPoints[fill=black](D)
    
    \node [label={0+angulo_de_giro}:A] at (A){{}};
    \node [label={162+angulo_de_giro}:B] at (B){{}};
    \node [label={270+angulo_de_giro}:C] at (C){{}};
    \node [label={270+angulo_de_giro}:D] at (D){{}};

    \draw pic["${letra_A}$",draw,-,angle radius=1cm, dashed] {{angle=D--C--A}};
    \draw pic["${letra_B}$",draw,-,angle radius=0.8cm, dashed] {{angle=A--C--B}};
    \draw pic["{Matematica(angulo_2+"°")}",draw,-,angle radius=1cm] {{angle=C--B--A}};

    \end{{tikzpicture}} \end{{center}}
    {Matematica(letra_A+"+"+letra_B+"=")}"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(180-angulo_1/2, cargar_decimal=True)+"°")
    contenido_2 = Matematica(Racional(180-angulo_1/2+angulo_2, cargar_decimal=True)+"°")
    contenido_3 = Matematica(Racional(180-angulo_1/2+2*angulo_2, cargar_decimal=True)+"°")
    contenido_4 = Matematica(Racional(180-angulo_1/2+angulo_2/2, cargar_decimal=True)+"°")
    contenido_5 = Matematica(Racional(180-2*angulo_1, cargar_decimal=True)+"°")


elif opcion==14:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    angulo_1 = Racional(choice([2,3,4,5,6,8,9,10]))
    angulo_2 = Racional(randrange(10,45))
    while 360/angulo_1-2*angulo_2<=0:
        angulo_1 = Racional(choice([2,3,4,5,6,8,9,10]))
        angulo_2 = Racional(randrange(10,45))
    diccionario_numero_parte = {2:"la mitad", 3:"un tercio", 4:"un cuarto", 5:"un quinto", 6:"un sexto", 8:"un octavo", 9:"un noveno", 10:"un décimo"}
    angulo_de_giro = choice([0,180])+randrange(-40,40)
    letras = [r"\alpha", r"\beta", r"\delta"]
    shuffle(letras)
    letra_A, letra_B = letras[0], letras[1]

    #================================Aquí va el enunciado================================================================
    enunciado = f"En la siguiente figura, el arco EA es {diccionario_numero_parte[int(angulo_1)]} del arco completo y "+Matematica(Fr"\angle ECA={angulo_2}°",arreglar_espacios=False)+fr"""
    \begin{{center}} \begin{{tikzpicture}} [scale=2]

    \draw (0,0) circle(1);

    \tkzDefPoint({randrange(230,240)+angulo_de_giro}:1){{A}}
    \tkzDefPoint({randrange(-25,-15)+angulo_de_giro}:1){{B}}
    \tkzDefPoint({randrange(15,25)+angulo_de_giro}:1){{D}}
    \tkzDefPoint({randrange(120,130)+angulo_de_giro}:1){{E}}
    \tkzInterLL(E,D)(A,B) \tkzGetPoint{{C}}

    \node [label={225+angulo_de_giro}:A] at (A){{}};
    \node [label={-25+angulo_de_giro}:B] at (B){{}};
    \node [label={0+angulo_de_giro}:C] at (C){{}};
    \node [label={25+angulo_de_giro}:D] at (D){{}};
    \node [label={135+angulo_de_giro}:E] at (E){{}};

    \tkzDrawSegment(E,C)
    \tkzDrawSegment(A,C)

    \draw pic["{Matematica(angulo_2+"°")}",draw,angle radius=1.1cm] {{angle=E--C--A}};

    \end{{tikzpicture}} \end{{center}}
    El arco BD"""
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Racional(360/angulo_1-2*angulo_2,cargar_decimal=True)+"°")
    contenido_2 = Matematica(Racional(360/angulo_1-angulo_2,cargar_decimal=True)+"°")
    contenido_3 = Matematica(Racional(360/angulo_1-angulo_2/2,cargar_decimal=True)+"°")
    contenido_4 = Matematica(Racional(abs(180/angulo_1-2*angulo_2),cargar_decimal=True)+"°")
    contenido_5 = Matematica(Racional(abs(180/angulo_1-angulo_2),cargar_decimal=True)+"°")



enunciado_oculto = [opcion, contenido_correcto]











