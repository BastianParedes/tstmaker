{"cantidad_opciones":6, "cantidad_disponible":50}


lista_de_letras = ["x","y","z","w"]
shuffle(lista_de_letras)
letra_x, letra_y, letra_z, letra_w = lista_de_letras[0], lista_de_letras[1], lista_de_letras[2], lista_de_letras[3]

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    resultado = randrange(1,10)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(logaritmo(fraccion(Pol({letra_x:resultado+1},{letra_x:resultado},azar=True),Pol(letra_x,1,azar=True)),letra_x, parentesis_automatico=False)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(resultado)
    contenido_2 =        Matematica(letra_x)
    contenido_3 =        Matematica(potencia(letra_x,resultado))
    contenido_4 =        Matematica(potencia(resultado,letra_x))
    contenido_5 =        Matematica(choice([Fraction(letra_x,resultado,simplificar=True), Fraction(resultado,letra_x)]))
    enunciado_oculto = [opcion, resultado]

elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    pol_1, pol_2 = Pol(letra_x, elegir(-9,10,0)), Pol(letra_x, elegir(-9,10,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(logaritmo(fraccion(pol_1*pol_2,pol_1), pol_2, parentesis_automatico=False)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(1)
    contenido_2 =        Matematica(pol_1)
    contenido_3 =        Matematica(pol_2)
    contenido_4 =        Matematica(0)
    contenido_5 =        Matematica(-1)
    enunciado_oculto = [opcion]


elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    pol_1, pol_2 = Pol(letra_x, elegir(-9,10,0)), Pol(letra_x, elegir(-9,10,0))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(logaritmo(fraccion(pol_1,pol_1*pol_2), pol_2, parentesis_automatico=False)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(-1)
    contenido_2 =        Matematica(pol_1)
    contenido_3 =        Matematica(pol_2)
    contenido_4 =        Matematica(0)
    contenido_5 =        Matematica(1)
    enunciado_oculto = [opcion]


elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    pol_1 = Pol(letra_x, randrange(-5,6))*Pol(letra_x, randrange(-5,6))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(logaritmo(1,pol_1, parentesis_automatico=False)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(0)
    contenido_2 =        Matematica(1)
    contenido_3 =        Matematica(-1)
    contenido_4 =        Matematica(2)
    contenido_5 =        Matematica(-2)
    enunciado_oculto = [opcion]


elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    exponente_1, exponente_2 = Racional(randrange(1,20), randrange(2,20)), Racional(randrange(1,20), randrange(2,20))
    while exponente_1.numerador==1 or exponente_1.denominador==1 or exponente_2.numerador==1 or exponente_2.denominador==1:
        exponente_1, exponente_2 = Racional(randrange(1,20), randrange(2,20)), Racional(randrange(1,20), randrange(2,20))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(logaritmo(raiz(potencia(letra_x,exponente_1.numerador,quitar_1=True),exponente_1.denominador), raiz(potencia(letra_x,exponente_2.numerador,quitar_1=True),exponente_2.denominador), parentesis_automatico=False)+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(exponente_1/exponente_2)
    contenido_2 =        Matematica(exponente_1*exponente_2)
    contenido_3 =        Matematica(exponente_1-exponente_2)
    contenido_4 =        Matematica(exponente_1+exponente_2)
    contenido_5 =        Matematica(choice([exponente_1,exponente_2]))
    enunciado_oculto = [opcion, exponente_1,exponente_2]


elif opcion==6:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    term_1, term_2 = letra_x*Racional(randrange(1,10)), letra_x*Racional(randrange(1,10))
    exponente_1, exponente_2 = Racional(randrange(1,4)), Racional(randrange(1,4))
    base = Racional(choice([2,3,4]))
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(logaritmo(potencia(base**exponente_1,term_1), potencia(base**exponente_2,term_2))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(term_1*exponente_1/(term_2*exponente_2))
    contenido_2 =        Matematica(term_1/term_2)
    contenido_3 =        Matematica(exponente_1/exponente_2)
    contenido_4 =        Matematica(term_1*exponente_1+term_2*exponente_2)
    contenido_5 =        Matematica(term_1*exponente_1-term_2*exponente_2)
    enunciado_oculto = [opcion, term_1, term_2, exponente_1, exponente_2]












