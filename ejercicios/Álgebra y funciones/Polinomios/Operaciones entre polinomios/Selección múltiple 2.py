{"cantidad_opciones":3, "cantidad_disponible":50}

unidadDeMedida = choice(["mm", "cm", "m", "km"])


if opcion==1:
    opcion_b = choice([1,2])
    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        while True:
            a, b, c, d = elegir(-9,10,0), elegir(-9,10,0), elegir(-9,10,0), elegir(-9,10,0)
            if a != b != c != d:
                break
        p1, p2, p3, p4 = Pol("x",a,parentesis=True), 2*Pol("x",b,parentesis=True), 2*Pol("x",c,parentesis=True), Pol("x",d,parentesis=True)
        #================================Aquí va el enunciado================================================================
        enunciado = fr"""En la siguiente figura se cumple que A, B y C son colineales, B, F y D son colineales, ABFE es rectángulo, AE mide {Matematica(p1+" "+unidadDeMedida)}, AB mide {Matematica(p2+" "+unidadDeMedida)}, BC mide {Matematica(p3+" "+unidadDeMedida)} y DF mide {Matematica(p4+" "+unidadDeMedida)}
\begin{{center}} \begin{{tikzpicture}} [scale=1.8, rotate={randrange(0,360)}]
\coordinate (A) at (-1.5 , 1);
\coordinate (B) at (-1.5 , 0);
\coordinate (C) at (-1.5 , -1);
\coordinate (D) at (1 ,0);
\coordinate (E) at (0 , 1);
\coordinate (F) at (0 , 0);

\draw (E) -- (A) -- (C) -- (D) -- (E) -- (F);
\draw (B) -- (D);

\tkzMarkRightAngle[size=0.15](C,B,D)
\tkzMarkRightAngle[size=0.15](D,F,E)

\node at ($(A)+(135:0.15)$) {{A}};
\node at ($(B)+(180:0.15)$) {{B}};
\node at ($(C)+(225:0.15)$) {{C}};
\node at ($(D)+(0:0.15)$) {{D}};
\node at ($(E)+(45:0.15)$) {{E}};
\node at ($(F)+(-90:0.15)$) {{F}};

\end{{tikzpicture}} \end{{center}}
Calcula una expresión para el área de la figura ABCDE"""
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica("("+ (p1*p2 + p3*(p1+p4)/2 + p2*p4/2) + ") "+potencia(unidadDeMedida,2,parentesis_automatico=False))
        contenido_2 =        Matematica("("+ p1*p2 + ") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcula solo el área del rectángulo
        contenido_3 =        Matematica("("+ p3*(p1+p4) + ") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcula solo el área de triángulo de abajo
        contenido_4 =        Matematica("("+ p2*p4 + ") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcujla sol el área del triángulo de la derecha
        contenido_5 =        Matematica("("+ (p1*p2 + p3*(p1+p4)/2 + p2*p4) + ") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # No divide endos al calcular las áreas de los triángulos
        enunciado_oculto = [opcion, opcion_b, p1,p2,p3,p4]



    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        while True:
            a, b, c, d = elegir(-9,10,0), elegir(-9,10,0), elegir(-9,10,0), elegir(-9,10,0)
            if a != b != c != d and (b+c)%2 == 0:
                break
        p1, p2, p3, p4 = Pol("x",a,parentesis=True), Pol("x",b,parentesis=True), Pol("x",c,parentesis=True), Pol("x",d,parentesis=True)
        #================================Aquí va el enunciado================================================================
        enunciado = fr"""En la siguiente figura se cumple que B, F, y E son colineales, BCDE es rectángulo, DE mide {Matematica(p1+" "+unidadDeMedida)}, FB mide {Matematica(p2+" "+unidadDeMedida)}, FE mide {Matematica(p3+" "+unidadDeMedida)} y FA mide {Matematica(p4+" "+unidadDeMedida)}
\begin{{center}} \begin{{tikzpicture}} [scale=1.8, rotate={randrange(0,360)}]
\coordinate (A) at (0 , 1);
\coordinate (B) at (-1 , 0);
\coordinate (C) at (-1 , -0.5);
\coordinate (D) at (1.5 , -0.5);
\coordinate (E) at (1.5 , 0);
\coordinate (F) at (0 , 0);

\draw (B) -- (C) -- (D) -- (E) -- (B) -- (A) -- (E);
\draw [dashed] (A) -- (F);

\tkzMarkRightAngle[size=0.15](E,F,A)

\node at ($(A)+(90:0.15)$) {{A}};
\node at ($(B)+(180:0.15)$) {{B}};
\node at ($(C)+(225:0.15)$) {{C}};
\node at ($(D)+(-45:0.15)$) {{D}};
\node at ($(E)+(0:0.15)$) {{E}};
\node at ($(F)+(-90:0.15)$) {{F}};

\end{{tikzpicture}} \end{{center}}
Calcula una expresión para el área de la figura ACDE"""
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica("("+ (p1*(p2+p3) + p4*(p2+p3)/2) +") "+potencia(unidadDeMedida,2,parentesis_automatico=False))
        contenido_2 =        Matematica("("+ p1*(p2+p3) +") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcula solo el área del rectángulo
        contenido_3 =        Matematica("("+ p4*(p2+p3)/2 + ") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcula solo el área de triángulo
        contenido_4 =        Matematica("("+ p4*(p2+p3) +") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcula solo el área de triángulo, pero sin dividir en dos
        contenido_5 =        Matematica("("+ (p1*(p2+p3) + p4*(p2+p3) )+") "+potencia(unidadDeMedida,2,parentesis_automatico=False)) # Calcula el área de todo, pero sin dividir el área del triángulo en 2
        enunciado_oculto = [opcion, opcion_b, p1,p2,p3,p4]



elif opcion==2:
    opcion_b = choice([1,2,3])
    if opcion_b == 1:
        #================================Aquí va el enunciado================================================================
        enunciado = "Sea un número entero n. El producto entre su antecesor y su sucesor está dado por la expresión"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Pol("n",-1) * Pol("n",1))
        contenido_2 =        Matematica(Pol("n", -1))
        contenido_3 =        Matematica(Pol("n",1))
        contenido_4 =        Matematica("n"*Pol("n",-1))
        contenido_5 =        Matematica("n"*Pol("n",1))

    elif opcion_b == 2:
        #================================Aquí va el enunciado================================================================
        enunciado = "Sea un número entero par n. Si el n es multiplicado por su par consecutivo se obtiene la expresión"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica("n" * Pol("n",2))
        contenido_2 =        Matematica("n" * Pol("n", 1))
        contenido_3 =        Matematica(Pol("n",2))
        contenido_4 =        Matematica(potencia("n",2))
        contenido_5 =        Matematica("n" * Pol("n",-1))

    elif opcion_b == 3:
        #================================Aquí va el enunciado================================================================
        enunciado = "Sea el número entero impar n. El producto entre el sucesor de n y su impar anterior está dado por la expresión"
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = Matematica(Pol("n",1) * Pol("n",-2))
        contenido_2 =        Matematica(Pol("n",-1) * Pol("n",2))
        contenido_3 =        Matematica(Pol("n",-1) * Pol("n",1))
        contenido_4 =        Matematica("n" * Pol("n",1))
        contenido_5 =        Matematica("n" * Pol("n",-2))


    enunciado_oculto = [opcion, opcion_b]



elif opcion==3:
    a, b, c, d = Racional(elegir(-5,6, 0,1)) , Racional(elegir(-5,6, 0,1)) , Racional(elegir(-5,6, 0,1)) , Racional(elegir(-5,6, 0,1))
    p1,p2 = Pol("x",b) , Pol("x",d,parentesis=True)
    linea1 = Pol(a*potencia(p1,2) , c*p2.show)

    opcion_b = choice([1,2,3,4,5])

    if opcion_b==1:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        b = -b
        p1,p2 = Pol("x",b) , Pol("x",d,parentesis=True)
        linea2 = Pol(a*("("+p1**2 +")") , c*p2.show)
        linea3 = Pol((a*p1**2).show , c*p2.show)
        linea4 = Pol((a*p1**2).show , (c*p2).show)
        linea5 = Pol(Term(a,{"x":2}) , (2*a*b+c)*"x" , a*b**2  , c*d)
        linea6 = a*p1**2 + c*p2
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = "Paso 1"
        contenido_2 =        "Paso 2"
        contenido_3 =        "Paso 3"
        contenido_4 =        "Paso 4"
        contenido_5 =        "Paso 5"

    elif opcion_b==2:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        linea2 = Pol(a*("("+p1**2 +")") , c*p2.show)
        a, b = -a, -b
        p1,p2 = Pol("x",b) , Pol("x",d,parentesis=True)
        linea3 = Pol((a*p1**2).show , c*p2.show)
        linea4 = Pol((a*p1**2).show , (c*p2).show)
        linea5 = Pol(Term(a,{"x":2}) , (2*a*b+c)*"x" , a*b**2  , c*d)
        linea6 = a*p1**2 + c*p2
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = "Paso 2"
        contenido_2 =        "Paso 3"
        contenido_3 =        "Paso 4"
        contenido_4 =        "Paso 5"
        contenido_5 =        "Paso 1"

    elif opcion_b==3:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        linea2 = Pol(a*("("+p1**2 +")") , c*p2.show)
        linea3 = Pol((a*p1**2).show , c*p2.show)
        d = -d
        p1,p2 = Pol("x",b) , Pol("x",d,parentesis=True)
        linea4 = Pol((a*p1**2).show , (c*p2).show)
        linea5 = Pol(Term(a,{"x":2}) , (2*a*b+c)*"x" , a*b**2  , c*d)
        linea6 = a*p1**2 + c*p2
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = "Paso 3"
        contenido_2 =        "Paso 4"
        contenido_3 =        "Paso 5"
        contenido_4 =        "Paso 1"
        contenido_5 =        "Paso 2"

    elif opcion_b==4:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        linea2 = Pol(a*("("+p1**2 +")") , c*p2.show)
        linea3 = Pol((a*p1**2).show , c*p2.show)
        linea4 = Pol((a*p1**2).show , (c*p2).show)
        c = -c
        p1,p2 = Pol("x",b) , Pol("x",d,parentesis=True)
        linea5 = Pol(Term(a,{"x":2}) , (2*a*b+c)*"x" , a*b**2  , c*d)
        linea6 = a*p1**2 + c*p2
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = "Paso 4"
        contenido_2 =        "Paso 5"
        contenido_3 =        "Paso 1"
        contenido_4 =        "Paso 2"
        contenido_5 =        "Paso 3"

    elif opcion_b==5:
        #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
        linea2 = Pol(a*("("+p1**2 +")") , c*p2.show)
        linea3 = Pol((a*p1**2).show , c*p2.show)
        linea4 = Pol((a*p1**2).show , (c*p2).show)
        linea5 = Pol(Term(a,{"x":2}) , (2*a*b+c)*"x" , a*b**2  , c*d)
        c = -c
        p1,p2 = Pol("x",b) , Pol("x",d,parentesis=True)
        linea6 = a*p1**2 + c*p2
        #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
        contenido_correcto = "Paso 5"
        contenido_2 =        "Paso 1"
        contenido_3 =        "Paso 2"
        contenido_4 =        "Paso 3"
        contenido_5 =        "Paso 4"

    enunciado = fr"""A continuación se muestra el procedimiento para que la expresión {Matematica(linea1)} sea reducida
\begin{{center}} \begin{{tikzpicture}} [scale=1, rotate=0]
\node [anchor=west] at (0,0) {{{Matematica(linea1)}}};
\node [anchor=west] at (0,-1) {{{Matematica("="+linea2)}}};
\node [anchor=west] at (0,-2) {{{Matematica("="+linea3)}}};
\node [anchor=west] at (0,-3) {{{Matematica("="+linea4)}}};
\node [anchor=west] at (0,-4) {{{Matematica("="+linea5)}}};
\node [anchor=west] at (0,-5) {{{Matematica("="+linea6)}}};

\draw [->,bend right=75] (0,-0.1) to (0,-0.9);
\draw [->,bend right=75] (0,-1.1) to (0,-1.9);
\draw [->,bend right=75] (0,-2.1) to (0,-2.9);
\draw [->,bend right=75] (0,-3.1) to (0,-3.9);
\draw [->,bend right=75] (0,-4.1) to (0,-4.9);

\node [anchor=east] at (-0.35,-0.5) {{Paso 1}};
\node [anchor=east] at (-0.35,-1.5) {{Paso 2}};
\node [anchor=east] at (-0.35,-2.5) {{Paso 3}};
\node [anchor=east] at (-0.35,-3.5) {{Paso 4}};
\node [anchor=east] at (-0.35,-4.5) {{Paso 5}};
\end{{tikzpicture}} \end{{center}} 
¿En qué paso se cometió el primer error?"""
    enunciado_oculto = [opcion, abs(a), abs(b), abs(c), abs(d)]










