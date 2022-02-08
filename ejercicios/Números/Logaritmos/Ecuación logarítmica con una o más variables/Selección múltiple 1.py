{"cantidad_opciones":7, "cantidad_disponible":50}

lista_de_letras = ["a", "b", "c", "x", "y"]
shuffle(lista_de_letras)
letra_1, letra_2, letra_3, letra_4, letra_5 = lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3], lista_de_letras[4]


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b = randrange(2,10), randrange(2,10)
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(letra_1,a)+"="+str(b))+f" entonces el valor de {letra_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(a**b)
    contenido_2 =        Matematica(b**a)
    contenido_3 =        Matematica(Root(a,b))
    contenido_4 =        Matematica(Root(b,a))
    contenido_5 =        Matematica(a*b)
    enunciado_oculto = [opcion,a,b]



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b = randrange(2,10), randrange(2,10)
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(a, letra_1)+"="+str(b))+f" entonces el valor de {letra_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(Root(a,b))
    contenido_2 =        Matematica(Root(b,a))
    contenido_3 =        Matematica(a**b)
    contenido_4 =        Matematica(b**a)
    contenido_5 =        Matematica(a*b)
    enunciado_oculto = [opcion,a,b]


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, x1 = Racional(elegir(-5,6, 0)), Racional(randrange(0, 10))
    a, b = a1, -a1*x1**2+1
    c, d, e = Racional(elegir(-5,6, 0)), Racional(elegir(-5,6, 0)), Racional(0)
    while a*x1+b<0 or c*x1+d<=0 or c*x1+d==1 or 2*(a-c**2)==0 or c+d==0:
        a1, x1 = Racional(elegir(-5,6, 0)), Racional(randrange(0, 10))
        a, b = a1, -a1*x1**2+1
        c, d, e = Racional(elegir(-5,6, 0)), Racional(elegir(-5,6, 0)), Racional(0)
    #================================Aquí va el enunciado================================================================
    # enunciado = "Si "+Matematica(fraccion(logaritmo(Pol(Term(a,{"x":2}),b,azar=True)), logaritmo(Pol(c*"x",d,azar=True)))+"="+letra_1**e)+f", entonces el valor de {letra_1} es"
    enunciado = "Si "+Matematica(logaritmo(Pol(Term(a,{letra_1:2}),b,azar=True), Pol(c*letra_1,d,azar=True))+"="+e)+f", entonces el valor de {letra_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x1)
    contenido_2 =        Matematica(Fraction( Pol(c,Root(abs(c**2-4*a*b-4*a*d)),reducir=True) , 2*a))
    contenido_3 =        Matematica(Fraction( Pol(2*c*d,Root(abs(4*c**2*d**2-4*(a-c**2)*(b-d**2))),reducir=True) , 2*(a-c**2)))
    contenido_4 =        Matematica((a+b)/(c+d))
    contenido_5 =        Matematica(0)
    enunciado_oculto = [opcion,a,b]



elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, x1, d, e = Racional(elegir(-5,6, 0)), Racional(randrange(0,10)), Racional(elegir(-5,6, 0)), Racional(1)
    a, b, c = a1, a1*x1**2+d, 2*a1*x1
    while a*x1**2+b<=0 or c*x1+d<=0 or c*x1+d==1 or a-c**2==0 or c+d==0:
        a1, x1, d, e = Racional(elegir(-5,6, 0)), Racional(randrange(0,10)), Racional(elegir(-5,6, 0)), Racional(1)
        a, b, c = a1, a1*x1**2+d, 2*a1*x1
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(Pol(Term(a,{letra_1:2}),b,azar=True), Pol(c*letra_1,d,azar=True))+"="+e)+f", entonces el valor de {letra_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x1)
    contenido_2 =        Matematica(Root(abs((1-b)/a)))
    contenido_3 =        Matematica(Fraction( Pol(2*c*d,Root(abs(4*c**2*d**2-4*(a-c**2)*(b-d**2))),reducir=True) , 2*(a-c**2)))
    contenido_4 =        Matematica((a+b)/(c+d))
    contenido_5 =        Matematica(1)
    enunciado_oculto = [opcion,a,b,c,d]



elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, x1, c, e = Racional(elegir(-5,6, 0)), Racional(randrange(1,10)), Racional(elegir(-5,6, 0)), Racional(2)
    a, d = a1+c**2, a1*x1/c
    b = a1*x1**2+d**2
    while  a*x1**2+b<=0 or c*x1+d<=0 or c*x1+d==1 or d.denominador!=1 or a-c**2==0 or c+d==0 or a-c==0:
        a1, x1, c, e = Racional(elegir(-5,6, 0)), Racional(randrange(1,10)), Racional(elegir(-5,6, 0)), Racional(2)
        a, d = a1+c**2, a1*x1/c
        b = a1*x1**2+d**2
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(Pol(Term(a,{letra_1:2}),b,azar=True), Pol(c*letra_1,d,azar=True))+"="+e)+f", entonces el valor de {letra_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x1)
    contenido_2 =        Matematica(Root(abs((1-b)/a)))
    contenido_3 =        Matematica(Fraction( Pol(2*c*d,-Root(abs(4*c**2*d**2-4*(a-c**2)*(b-d**2))),reducir=True) , 2*(a-c)))
    contenido_4 =        Matematica((a+b)/(c+d))
    contenido_5 =        Matematica(2)
    enunciado_oculto = [opcion,a,b,c,d]



elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, x1, d, e = Racional(elegir(-5,6, 0)), Racional(randrange(-9,10)), Racional(randrange(2,5)), Racional(randrange(0,6))
    a, b, c = a1, -2*a1*x1, a1*x1**2+d**e
    while a*x1**2+b*x1+c<=0:
        a1, x1, d, e = Racional(elegir(-5,6, 0)), Racional(randrange(-9,10)), Racional(randrange(2,5)), Racional(randrange(0,6))
        a, b, c = a1, -2*a1*x1, a1*x1**2+d**e
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(logaritmo(Pol(Term(a,{"x":2}),b*"x",c,azar=True), d) + "=" + e)+f", entonces el valor de {letra_1} es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(x1)
    contenido_2 =        Matematica(Fraction(Pol(-b,Root(abs(b**2-a*(c-d))),reducir=True), 2*a))
    contenido_3 =        Matematica(Fraction(Pol(-b,Root(abs(b-4*a*(c-d*e))),reducir=True), 2*a))
    contenido_4 =        Matematica(Fraction(Pol(b,Root(abs(b**2-4*a*(c-d**e))),reducir=True), 2))
    contenido_5 =        Matematica(Fraction(Pol(b,Root(abs(b-c-d**e)),reducir=True), 2*a))
    enunciado_oculto = [opcion,a,b,c,d,e]


elif opcion==7:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a, b, c, d = Racional(randrange(1,10)), Racional(randrange(1,10)), Racional(randrange(1,10)), Racional(randrange(1,4))
    base, a_1, b_1, c_1 = Racional(randrange(2,5)), Racional(choice([-1,1])), Racional(choice([-1,1])), Racional(choice([-1,1]))
    #================================Aquí va el enunciado================================================================
    enunciado = "Si "+Matematica(Pol(a_1*logaritmo(a*"x",base), b_1*logaritmo(b*"y",base), c_1*logaritmo(c*"z",base), azar=True)+"="+d)+" entonces el valor de "+Matematica(Term(1,{"x":int(a_1), "y":int(b_1), "z":int(c_1)}))+" es"
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(base**d/( a**a_1* b**b_1* c**c_1))
    contenido_2 =        Matematica(base**d* a**a_1* b**b_1* c**c_1)
    contenido_3 =        Matematica(base* a**a_1* b**b_1* c**c_1)
    contenido_4 =        Matematica(base* a**(-a_1)* b**(-b_1)* c**(-c_1))
    contenido_5 =        Matematica(d* a**a_1* b**b_1* c**c_1)
    enunciado_oculto = [a,b,c,d]










