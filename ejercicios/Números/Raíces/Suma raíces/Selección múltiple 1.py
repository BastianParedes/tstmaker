{"cantidad_opciones":2, "cantidad_disponible":50}


if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, b1 = Racional(elegir(1,10,0)), Racional(elegir(1,10,0))
    while abs(a1)==abs(b1):
        a1, b1 = Racional(elegir(-9,10,0)), Racional(elegir(-9,10,0))
    a2, b2 = Racional(randrange(2,7))**2, Racional(randrange(2,7))**2
    while a2==b2:
        a2, b2 = Racional(randrange(2,7))**2, Racional(randrange(2,7))**2
    x = randrange(2,11)
    while isinstance(Root(x), Racional):
        x = randrange(2,11)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a1*Root(a2*x), b1*Root(b2*x))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((a1*a2+b1*b2)*Root(x))
    contenido_2 = Matematica((a1*a2**2+b1*b2**2)*Root(x))#No calcula la raíz al descomponer
    contenido_3 = Matematica(Root(x))#Descompone la raíz, pero no suma ni multiplica nada
    contenido_4 = Matematica((a1+b1)*Root((a2+b2)*x))#suma partes descompuestas entre ellas y las raíces entre ellas.
    contenido_5 = Matematica((a1+a2+b1+b2)*Root(x))#Suma al momento de descomponer
    enunciado_oculto = [x, a1, a2, b1, b2]



elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    a1, b1, c1 = Racional(elegir(1,10,0)), Racional(elegir(1,10,0)), Racional(elegir(1,10,0))
    while abs(a1)==abs(b1) or abs(b1)==abs(c1) or abs(a1)==abs(c1):
        a1, b1, c1 = Racional(elegir(-9,10,0)), Racional(elegir(-9,10,0)), Racional(elegir(-9,10,0))
    a2, b2, c2 = Racional(randrange(2,7))**2, Racional(randrange(2,7))**2, Racional(randrange(2,7))**2
    while a2==b2 or b2==c2 or a2==c2:
        a2, b2, c2 = Racional(randrange(2,7))**2, Racional(randrange(2,7))**2, Racional(randrange(2,7))**2
    x = randrange(2,11)
    while isinstance(Root(x), Racional):
        x = randrange(2,11)
    #================================Aquí va el enunciado================================================================
    enunciado = Matematica(Pol(a1*Root(a2*x), b1*Root(b2*x), c1*Root(c2*x))+"=")
    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica((a1*a2+b1*b2+c1*c2)*Root(x))
    contenido_2 = Matematica((a1*a2**2+b1*b2**2+c1*c2**2)*Root(x))#No calcula la raíz al descomponer
    contenido_3 = Matematica(Root(x))#Descompone la raíz, pero no suma ni multiplica nada
    contenido_4 = Matematica((a1+b1+c1)*Root((a2+b2+c2)*x))#suma partes descompuestas entre ellas y las raíces entre ellas.
    contenido_5 = Matematica((a1+a2+b1+b2+c1+c2)*Root(x))#Suma al momento de descomponer
    enunciado_oculto = [x, a1, a2, b1, b2, c1, c2]













